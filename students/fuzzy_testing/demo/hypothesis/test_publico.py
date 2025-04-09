import requests
from hypothesis import given, strategies as st, settings
from hypothesis import HealthCheck
from hypothesis.strategies import text, integers

BASE_URL = "https://jsonplaceholder.typicode.com"

settings.register_profile("no_deadline", deadline=None)
settings.load_profile("no_deadline")


# testeamos /posts/{id}
# @settings(suppress_health_check=[HealthCheck.flaky])
# @settings(deadline=500)
@given(post_id=st.integers(min_value=1, max_value=100))
def test_public_post_api(post_id):
    url = f"{BASE_URL}/posts/{post_id}"
    response = requests.get(url)
    assert response.status_code == 200
    post = response.json()
    assert "userId" in post
    assert "id" in post
    assert "title" in post
    assert "body" in post
    assert isinstance(post["title"], str)
    assert isinstance(post["body"], str)
    assert 1 <= post["id"] <= 100


# testeamos /posts?userId=X
# @settings(suppress_health_check=[HealthCheck.flaky])
@given(user_id=st.integers(min_value=1, max_value=10))
def test_posts_by_user(user_id):
    response = requests.get(f"{BASE_URL}/posts?userId={user_id}")
    assert response.status_code == 200
    posts = response.json()
    for post in posts:
        assert post["userId"] == user_id
        assert isinstance(post["title"], str)
        assert isinstance(post["body"], str)


# testeamos que cada /post tenga comentarios relacionados
@given(post_id=st.integers(min_value=1, max_value=100))
def test_post_has_comments(post_id):
    comments = requests.get(f"{BASE_URL}/comments?postId={post_id}").json()
    for comment in comments:
        assert "postId" in comment and comment["postId"] == post_id
        assert "email" in comment and "@" in comment["email"]
        assert isinstance(comment["body"], str)


# /users/{id} con validaciones complejas
@given(user_id=st.integers(min_value=1, max_value=10))
def test_user_schema(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    user = response.json()
    assert isinstance(user["name"], str)
    assert isinstance(user["username"], str)
    assert isinstance(user["email"], str)
    assert "address" in user and isinstance(user["address"], dict)
    address = user["address"]
    assert "city" in address and isinstance(address["city"], str)
    assert "geo" in address
    geo = address["geo"]
    assert "lat" in geo and "lng" in geo


# test combinado: user → posts → comments
@given(user_id=st.integers(min_value=1, max_value=10))
def test_user_posts_have_comments(user_id):
    posts = requests.get(f"{BASE_URL}/posts?userId={user_id}").json()
    for post in posts:
        post_id = post["id"]
        comments = requests.get(f"{BASE_URL}/comments?postId={post_id}").json()
        assert isinstance(comments, list)
        for comment in comments:
            assert comment["postId"] == post_id
            assert "email" in comment and "@" in comment["email"]


# test fallos esperados con inputs inválidos
@given(bad_id=text(min_size=1, max_size=10).filter(lambda s: not s.isdigit()))
def test_invalid_post_id(bad_id):
    response = requests.get(f"{BASE_URL}/posts/{bad_id}")
    assert response.status_code in (404, 400)

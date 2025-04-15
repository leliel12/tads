from app import app
from hypothesis import given, strategies as st

def client():
    app.testing = True
    return app.test_client()

# suma valida
@given(a=st.integers(), b=st.integers())
def test_sum_endpoint_with_valid_ints(a, b):
    response = client().get(f"/sum?a={a}&b={b}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["result"] == a + b

# sumando texto
@given(text=st.text().filter(lambda x: not x.isdigit()))
def test_sum_endpoint_with_invalid_input(text):
    response = client().get(f"/sum?a={text}&b=1")
    # if not text.isdigit():
    assert response.status_code == 400
        

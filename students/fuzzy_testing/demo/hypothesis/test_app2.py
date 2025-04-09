from app import app
from hypothesis import given, strategies as st
from datetime import date


def client():
    app.testing = True
    return app.test_client()


valid_emails = st.emails()
valid_passwords = st.text(min_size=6, max_size=20) 
valid_birthdates = st.dates(min_value=date(1900, 1, 1), max_value=date.today()).map(
    lambda d: d.isoformat()
)

invalid_passwords = st.text()
invalid_birthdates = st.dates().map(
    lambda d: d.isoformat()
)


@given(email=valid_emails, password=valid_passwords, birthdate=valid_birthdates)
def test_register_valid_inputs(email, password, birthdate):
    response = client().post(
        "/register", json={"email": email, "password": password, "birthdate": birthdate}
    )
    assert response.status_code == 200
    assert response.get_json()["status"] == "registered"


#################################################################


@given(
    email=st.text(min_size=1, max_size=50).filter(lambda x: "@" not in x),
    password=st.text(min_size=1, max_size=5),
    birthdate=st.text(min_size=1, max_size=10),
)
def test_register_invalid_inputs(email, password, birthdate):
    response = client().post(
        "/register", json={"email": email, "password": password, "birthdate": birthdate}
    )
    assert response.status_code == 400


# fechas futuras
from datetime import timedelta

@given(
    email=valid_emails,
    password=valid_passwords,
    birthdate=st.just((date.today() + timedelta(days=1)).isoformat()),
)
def test_future_birthdate_rejected(email, password, birthdate):
    response = client().post(
        "/register", json={"email": email, "password": password, "birthdate": birthdate}
    )
    assert response.status_code == 400


#################################################################

from hypothesis import given
from hypothesis.strategies import composite

# todo el JSON de una
@composite
def user_payload(draw):
    email = draw(valid_emails)
    password = draw(valid_passwords)
    birthdate = draw(valid_birthdates)
    return {"email": email, "password": password, "birthdate": birthdate}


@composite
def weak_user_payload(draw):
    email_username = draw(st.text(min_size=3, max_size=10).filter(lambda x: x.isalnum()))
    domain = draw(st.sampled_from(["hotmail.com", "yahoo.com", "mail.com"]))
    email = f"{email_username}@{domain}"
    
    # Password que incluye el username
    password_suffix = draw(st.text(min_size=2, max_size=6))
    password = f"{email_username}{password_suffix}"
    
    birthdate = draw(st.dates(min_value=date(1900, 1, 1), max_value=date.today())).isoformat()
    
    return {
        "email": email,
        "password": password,
        "birthdate": birthdate
    }


@given(payload=weak_user_payload())
def test_register_composite(payload):
    response = client().post("/register", json=payload)
    assert response.status_code == 200

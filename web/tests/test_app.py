import requests

BASE_URL = "http://127.0.0.1:5000"

def test_home_page_loads():
    response = requests.get(BASE_URL)
    assert response.status_code == 200

def test_short_password_rejected():
    response = requests.post(BASE_URL, data={"password": "short"}, allow_redirects=False)
    assert response.status_code == 200
    assert "8 characters" in response.text

def test_common_password_rejected():
    response = requests.post(BASE_URL, data={"password": "password"}, allow_redirects=False)
    assert response.status_code == 200
    assert "too common" in response.text

def test_valid_password_accepted():
    response = requests.post(BASE_URL, data={"password": "correcthorse"}, allow_redirects=True)
    assert response.status_code == 200
    assert "Welcome" in response.text
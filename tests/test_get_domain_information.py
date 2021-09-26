from main import app

from starlette.testclient import TestClient


client = TestClient(app)


def test_valid_domain():
    response = client.get("/?domain=stackoverflow.com")
    assert response.status_code == 200


def test_invalid_domain_with_path():
    response = client.get("/?domain=https://stackoverflow.com/test")
    assert response.status_code == 400


def test_invalid_domain_https():
    response = client.get("/?domain=https://stackoverflow.com")
    assert response.status_code == 400

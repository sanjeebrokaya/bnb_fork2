# Create your tests here.
from django.urls import reverse


def test_valid_login(manager_client, valid_login_form, client):
    """Test login with valid credentials"""
    response = client.get(reverse("accounts:login"))
    assert response.status_code == 200
    response = client.post(reverse("accounts:login"), data=valid_login_form)
    # Check that the login was successful (e.g., redirect or success message)
    assert response.status_code == 200


def test_create_staff_by_manager(manager_client):
    response = manager_client.get(reverse("accounts:create_staff"))
    assert response.status_code == 200

def test_create_staff_by_guest(guest_client):
    response = guest_client.get(reverse("accounts:create_staff"))
    assert response.status_code == 403



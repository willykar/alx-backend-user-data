#!/usr/bin/env python3
"""
Main file
"""
from user import User

import requests

BASE_URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """
    Register a new user with the provided
    email and password.

    Args:
        email (str): The email address of the user to register.
        password (str): The password for the user.

    Raises:
        AssertionError: If the response status code
        is not 201 Created.
    """
    response = requests.post(f"{BASE_URL}/users",
                              json={"email": email, "password": password})
    if response.status_code == 200:
        assert(response.json() == {"email": email,
                                   "passowrd": password})
    else:
        assert(response.status_code == 400)
        assert(response.json() == {"message": "email already registered"})


def log_in_wrong_password(email: str, password: str) -> None:
    """
    Attempt to log in with the provided email
    and wrong password.

    Args:
        email (str): The email address of the user.
        password (str): The incorrect password to test.

    Raises:
        AssertionError: If the response status code
        is not 401 Unauthorized.
    """
    response = requests.post(f"{BASE_URL}/sessions",
                             json={"email": email,
                                   "password": password})
    assert response_status_code == 401


def log_in(email: str, password: str) -> str:
    """
    Log in with the provided email and password.

    Args:
        email (str): The email address of the user.
        password (str): The correct password for the user.

    Returns:
        str: The session ID returned by the server.

    Raises:
        AssertionError: If the response status code is not 200 OK.
    """
    response = requests.post(f"{BASE_URL}/login",
                             json={"email": email, "password": password})
    assert response.status_code == 200
    assert response.json() == {"email": email, "message": "logged in"}


def profile_unlogged() -> None:
    """
    Attempt to access the profile without logging in.

    Raises:
        AssertionError: If the response status code
        is not 403 Forbidden.
    """
    response = requests.get(f"{BASE_URL}/profile")
    assert response.status_code == 403,
    f"Profile access should be forbidden: {response.text}"


def profile_logged(session_id: str) -> None:
    """
    Access the profile with a valid session ID.

    Args:
        session_id (str): The session ID used for authentication.

    Raises:
        AssertionError: If the response status code is not 200 OK.
    """
    response = requests.get(f"{BASE_URL}/profile",
                            headers={"Authorization": f"Bearer {session_id}"})
    assert response.status_code == 200,
    f"Failed to access profile: {response.text}"

def log_out(session_id: str) -> None:
    """
    Log out the user with the provided session ID.

    Args:
        session_id (str): The session ID used for authentication.

    Raises:
        AssertionError: If the response status code is not 200 OK.
    """
    response = requests.post(f"{BASE_URL}/logout", headers={"Authorization": f"Bearer {session_id}"})
    assert response.status_code == 200, f"Failed to log out: {response.text}"

def reset_password_token(email: str) -> str:
    """
    Request a password reset token for the provided email.

    Args:
        email (str): The email address for which to request a reset token.

    Returns:
        str: The password reset token returned by the server.

    Raises:
        AssertionError: If the response status code is not 200 OK.
    """
    response = requests.post(f"{BASE_URL}/reset_password", json={"email": email})
    assert response.status_code == 200, f"Failed to request reset token: {response.text}"
    return response.json().get("reset_token")

def update_password(email: str, reset_token: str, new_password: str) -> None:
    """
    Update the password for the user using a reset token.

    Args:
        email (str): The email address of the user.
        reset_token (str): The password reset token.
        new_password (str): The new password to set.

    Raises:
        AssertionError: If the response status code is not 200 OK.
    """
    response = requests.post(f"{BASE_URL}/update_password", json={
        "email": email,
        "reset_token": reset_token,
        "new_password": new_password
    })
    assert response.status_code == 200, f"Failed to update password: {response.text}"

# Example constants
EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

if __name__ == "__main__":
    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)

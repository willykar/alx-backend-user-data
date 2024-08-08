#!/usr/bin/env python3
"""
Basic Auth module
"""

from api.v1.auth.auth import Auth
from typing import TypeVar, List, Tuple, Optional
from models.user import User
import base64
import binascii


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth.
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> Optional[str]:
        """
        Returns the Base64 part of the Authorization
        header for Basic Authentication.
        """
        if (authorization_header is None or
                not isinstance(authorization_header, str) or
                not authorization_header.startswith("Basic ")):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> Optional[str]:
        """
        Returns the decoded value of a Base64 string.
        """
        if base64_authorization_header and isinstance(base64_authorization_header, str):
            try:
                encoded = base64_authorization_header.encode('utf-8')
                decoded = base64.b64decode(encoded)
                return decoded.decode('utf-8')
            except (binascii.Error, UnicodeDecodeError):
                return None
        return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[Optional[str], Optional[str]]:
        """
        Returns the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header and isinstance(decoded_base64_authorization_header, str):
            if ":" in decoded_base64_authorization_header:
                email, password = decoded_base64_authorization_header.split(":", 1)
                return email, password
        return None, None

    def authorization_header(self, request=None) -> Optional[str]:
        """
        Returns the Authorization header from a request object.
        """
        if request is None or not hasattr(request, 'headers'):
            return None
        return request.headers.get('Authorization', None)

    def user_object_from_credentials(self, email: Optional[str], password: Optional[str]) -> Optional[TypeVar('User')]:
        """
        Retrieves the User instance based on email and password.
        """
        if email is None or password is None:
            return None

        try:
            users = User.search({'email': email})
            for user in users:
                if user.is_valid_password(password):
                    return user
        except Exception as e:
            return None
        return None

    def current_user(self, request=None) -> Optional[TypeVar('User')]:
        """
        Overloads Auth and retrieves the User instance for a request.
        """
        header = self.authorization_header(request)
        if not header:
            return None

        b64header = self.extract_base64_authorization_header(header)
        if not b64header:
            return None

        decoded = self.decode_base64_authorization_header(b64header)
        if not decoded:
            return None

        email, password = self.extract_user_credentials(decoded)
        if not email or not password:
            return None

        return self.user_object_from_credentials(email, password)

#!/usr/bin/env python3
"""
basic_auth module
"""

# api/v1/auth/basic_auth.py

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic Authentication class that inherits from Auth """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization
        header for Basic Authentication.

        Args:
            authorization_header (str): The Authorization header.

        Returns:
            str: The Base64 encoded credentials part of the header,
            or None if invalid.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        # Extract the Base64 part by removing the "Basic " prefix
        return authorization_header[len("Basic "):]

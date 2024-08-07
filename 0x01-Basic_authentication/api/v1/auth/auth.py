#!/usr/bin/env python3
"""Authorization Class"""


from flask import Flask, request
from typing import List, TypeVar


class Auth():
    """"Class Authorization"""

    def require_auth(self, path: str, excluded_paths:
                     List[str]) -> bool:
        """ Determines if authentication is requied for
        given path"""
        return False

    def authorization_header(self, request=None) -> str:
        """Checks if Authorization request header
        is present and contain values"""
        if request is None or "Authorization" not in request.headers:
            return None
        else:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieves the current user based on the request
        Args:
            request: The flask request object
        Return:
            User
        """
        return None

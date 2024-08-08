#!/usr/bin/env python3
"""Authorization Class"""

from flask import Flask, request
from typing import List, TypeVar


class Auth:
    """Class Authorization"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines if authentication is required for the given path """

        if path is None:
            return True
        if not excluded_paths or not isinstance(excluded_paths, list):
            return True

        # Normalize the path by removing trailing slash
        normalized_path = path.rstrip('/') + '/'

        for excluded_path in excluded_paths:
            # Check if the excluded path ends with a wildcard '*'
            if excluded_path.endswith('*'):
                # Match the path up to the '*' in the excluded path
                if normalized_path.startswith(excluded_path[:-1]):
                    return False
                else:
                    # Normalize the excluded path by removing trailing slash
                    normalized_excluded_path = excluded_path.rstrip('/') + '/'
                    if normalized_path == normalized_excluded_path:
                        return False

        return True

    def authorization_header(self, request=None) -> str:
        """Checks if Authorization request header is present
        and contains values"""
        if request is None:
            return None

        if "Authorization" not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Retrieves the current user based on the request """
        return None

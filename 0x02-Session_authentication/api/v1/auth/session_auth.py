#!/usr/bin/env python3
"""
SessionAuth module for handling session-based authentication.
"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """
    SessionAuth class that inherits from Auth.
    Handles session-based authentication.
    """
    # Class attribute to store user_id by session_id
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user_id.
        
        Args:
            user_id (str): The ID of the user for whom the
            session is being created.
        
        Returns:
            str: The generated Session ID, or None if user_id is invalid.
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        # Generate a unique Session ID using uuid4
        session_id = str(uuid.uuid4())

        # Store the session_id and associated user_id in the 
        # class attribute dictionary
        self.user_id_by_session_id[session_id] = user_id

        return session_id

#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
import os

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize the auth variable
auth = None

# Load the appropriate authentication class based
# on the environment variable AUTH_TYPE
auth_type = os.getenv('AUTH_TYPE', 'auth')
if auth_type == 'session_auth':
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()
elif auth_type == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth_type == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()


@app.before_request
def before_request():
    """Filter each request before routing it to the corresponding view"""
    if auth is None:
        return

    # Paths that do not require authentication
    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                      '/api/v1/forbidden/', '/api/v1/auth_session/login/']

    # Check if the request path requires authentication
    if not auth.require_auth(request.path, excluded_paths):
        return

    # If both the Authorization header and session cookie are missing,
    # raise a 401 Unauthorized error
    if auth.authorization_header(request)
    is None and auth.session_cookie(request) is None:
        abort(401)

    # If the user cannot be authenticated, raise a 403 Forbidden error
    if auth.current_user(request) is None:
        abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized handler """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler """
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)

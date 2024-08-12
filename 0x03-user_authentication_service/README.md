# User Authentication Service

This project is a basic implementation of a user authentication system using Flask and SQLAlchemy. It includes functionalities such as user registration, login, session management, and password reset. This project is designed for educational purposes to help understand the underlying mechanisms of authentication systems.

## Project Structure

- **user.py**: Contains the SQLAlchemy model for the `User` entity.
- **db.py**: Provides database management functionalities, including adding, finding, and updating users.
- **auth.py**: Implements authentication logic, including user registration, password hashing, and session management.
- **app.py**: Sets up the Flask web application and provides routes for user registration, login, profile retrieval, and password reset.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/alx-backend-user-data.git
    cd alx-backend-user-data/0x03-user_authentication_service
    ```

2. **Set up a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Install `bcrypt`:**

    ```bash
    pip install bcrypt
    ```

## Usage

1. **Run the Flask application:**

    ```bash
    python app.py
    ```

    The Flask app will start and be accessible at `http://0.0.0.0:5000`.

2. **Endpoints:**

    - **POST /users**
    
        Registers a new user. Requires form data with `email` and `password`. 

        **Response:**
        - `{ "email": "<registered email>", "message": "user created" }` for successful registration.
        - `{ "message": "email already registered" }` with a 400 status code if the email is already registered.

    - **POST /sessions**
    
        Logs in a user. Requires form data with `email` and `password`.

        **Response:**
        - `{ "email": "<user email>", "message": "logged in" }` with a `Set-Cookie` header for session management.
        - `401 Unauthorized` if login credentials are incorrect.

    - **DELETE /sessions**
    
        Logs out a user by clearing the session.

        **Response:**
        - Redirects to GET `/`.

    - **GET /profile**
    
        Retrieves the profile of the logged-in user using the `session_id` cookie.

        **Response:**
        - `{ "email": "<user email>" }` with a `200 OK` status.
        - `403 Forbidden` if the session ID is invalid.

    - **POST /reset_password**
    
        Generates a password reset token. Requires form data with `email`.

        **Response:**
        - `{ "email": "<user email>", "reset_token": "<reset token>" }` with a `200 OK` status.
        - `403 Forbidden` if the email is not registered.

    - **PUT /reset_password**
    
        Updates the password using a reset token. Requires form data with `reset_token` and `new_password`.

        **Response:**
        - `{ "message": "Password updated successfully" }` with a `200 OK` status.
        - `403 Forbidden` if the reset token is invalid or expired.

## Requirements

- Python 3.7
- Flask
- SQLAlchemy 1.3.x
- bcrypt

## Testing

To test the endpoints, you can use tools like `curl` or Postman to send HTTP requests. The provided `main.py` scripts demonstrate how to interact with the API.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [bcrypt Documentation](https://pypi.org/project/bcrypt/)

Feel free to contribute or modify the project as needed for your learning purposes.



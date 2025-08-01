# Flask Recipe App Lab

This is a Flask REST API application that allows users to sign up, log in, manage sessions, and create/view recipes.  
The project demonstrates user authentication, session handling, password hashing, data validation, and serialization using Flask, Flask-RESTful, SQLAlchemy, Marshmallow, and Flask-Bcrypt.

## Features

- **User Registration:** Sign up with a unique username, password, image URL, and bio. Passwords are securely hashed.
- **Login & Logout:** Authenticate users and maintain sessions using cookies.
- **Auto-login:** Check session state to keep users logged in across requests.
- **Recipe Management:** Logged-in users can create and view recipes, each with a title, instructions (min 50 chars), and time to complete.
- **Data Validation:** Enforced at both model and API level with helpful error messages.
- **Serialization:** Users and recipes are serialized for easy frontend consumption.

## Endpoints

| Method | Endpoint       | Description                                   |
| ------ | -------------- | --------------------------------------------- |
| POST   | /signup        | Register a new user and auto-login            |
| GET    | /check_session | Return logged-in user info (auto-login check) |
| POST   | /login         | Log in an existing user                       |
| DELETE | /logout        | Log out the current user                      |
| GET    | /recipes       | Get all recipes (requires login)              |
| POST   | /recipes       | Create a new recipe (requires login)          |

## Error Handling

- All validation and integrity errors return helpful JSON error messages.
- Unauthorized access attempts return a 401 status code.

## Setup Instructions

1. **Clone the repository and set up a virtual environment:**

   ```sh
   pipenv install
   pipenv shell
   ```

2. **Run migrations to set up your database:**

   ```sh
   flask db upgrade
   ```

3. **(Optional) Seed your database:**

   ```sh
   python seed.py
   ```

4. **Run the Flask app:**

   ```sh
   python app.py
   ```

5. **Run tests:**
   ```sh
   pytest
   ```

## Technologies Used

- Flask & Flask-RESTful
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Bcrypt
- Marshmallow (serialization)
- Pytest (testing)

## Notes

- Only logged-in users can access or create recipes.
- Password hashes are never returned by the API.
- Validation and authentication are enforced on every endpoint.

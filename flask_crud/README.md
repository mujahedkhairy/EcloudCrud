# Flask CRUD Application

This is a simple Flask CRUD application for managing users. The application allows users to create, read, update, and delete user information, including username, password, and active status.

## Features

- User registration
- User login
- Display all users
- Update user information
- Delete users

## Technologies Used

- **Flask**: A lightweight WSGI web application framework.
- **Flask-SQLAlchemy**: An extension that adds support for SQLAlchemy to Flask applications.
- **Python-dotenv**: A library to read key-value pairs from a `.env` file into environment variables.

## Setup Instructions

Follow these steps to set up and run the application on your local machine:


1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/repository-name.git
   cd repository-name

2. Create a .env file in the root directory and add your secret key:
    SECRET_KEY=your_generated_secret_key

3. Install the required packages from requirements.txt:
    ```bash
    pip install -r requirements.txt

4. Run the application:
    ```bash
   python crud.py

5. Open your browser and navigate to http://127.0.0.1:5000 to access the application.


## Usage
### Register a User
- Navigate to the registration page.
- Enter a username and password.
- Click the "Register" button to create a new user.
### Login
- Navigate to the login page.
- Enter your username and password.
- Click the "Login" button to log in.
- Once logged in, you will be able to see the list of users.
### Manage Users
- View Users: You will see a list of all registered users.
- Edit User: Click the "Update" button next to a user to update their information.
- Delete User: Click the "Delete" button next to a user to remove them from the database.

## Acknowledgements

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/)
- [Python-dotenv Documentation](https://pypi.org/project/python-dotenv/)

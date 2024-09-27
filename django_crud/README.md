# Django CRUD Application

This is a simple Django CRUD application for managing users. The application allows users to create, read, update, and delete user information, including username, password, and active status.

## Features

- User registration
- User login
- Display all users
- Update user information
- Delete users

## Technologies Used

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design..
- **Django's Built-in ORM**: Provides a powerful database abstraction layer.
- **Django Messages Framework**: Used to display success and error messages to users.

## Setup Instructions

Follow these steps to set up and run the application on your local machine:


1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/repository-name.git
   cd repository-name

2. Create a virtual environment (optional but recommended):
    ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required packages from requirements.txt:
    ```bash
    pip install -r requirements.txt

4. Run database migrations:
    ```bash
    python manage.py migrate
   
5. Run the application:
    ```bash
    python manage.py runserver

6. Open your browser and navigate to http://127.0.0.1:8000 to access the application.


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

- [Django Documentation](https://docs.djangoproject.com/en/5.1/)


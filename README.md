# To-Do Web Application

A simple and intuitive To-Do web application built using Django. This app allows users to manage their tasks efficiently by adding, viewing, and deleting tasks.

## Features

- Add new tasks with a title and details.
- View a list of all tasks ordered by date and time stamp.
- Delete tasks when they are completed.
- User-friendly interface with Bootstrap for styling.

## Technologies Used

- **Backend**: Django 5.0.6 (Python)
- **Frontend**: HTML, CSS, Bootstrap 
- **Database**: SQLite (default configuration, can be changed to other databases)
- **Other**: JavaScript (for Bootstrap functionality)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/zaidkhuroo/todo-django-app.git
   cd todo-django-app
   
2. **Create a virtual environment:**
   ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`


3. **Apply migrations:**
   ```bash
    python manage.py makemigrations
    python manage.py migrate

4. **Run the development server:**
   ```bash
    python manage.py runserver

5. **Access the application:**
Open your web browser and go to http://127.0.0.1:8000/.

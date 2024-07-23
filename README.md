# School Portal

## Overview

School Portal is a Django-based web application designed to manage school-related activities. It allows users to register with different roles such as parent, student, teacher, and administrator. The portal provides functionalities for managing grades, schedules, and school news.

## Features

- User Registration and Authentication
- Role-based Access Control (Parent, Student, Teacher, Administrator)
- Grade Management
- Schedule Management
- News Management

## Requirements

- Python 3.x
- Django 3.x or higher

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/school_portal.git
    cd school_portal
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:8000/`.
2. Register a new account or log in with an existing account.
3. Navigate through the portal to manage grades, schedules, and news.

## Project Structure

school_portal/
├── app/
│ ├── migrations/
│ ├── templates/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── config/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── static/
│ ├── css/
│ ├── js/
│ └── images/
├── manage.py
├── requirements.txt
└── .gitignore


## Models

### CustomUser

A custom user model extending `AbstractUser` to include user roles and approval status.

### Schedule

Model to manage course schedules, including the course name, day of the week, start and end times, teacher, and students.

### Grade

Model to manage student grades for different courses.

### News

Model to manage news posts with a title, content, and creation date.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

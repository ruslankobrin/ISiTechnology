# Django REST API Application

This Django application provides REST endpoints for managing threads and messages.

## Prerequisites

- Python
- Django
- Django REST Framework

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/ruslankobrin/ISiTechnology.git
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Django development server:

    ```bash
    python manage.py runserver
    ```

2. Access the API endpoints:

    - To create a thread: `POST /threads/`
    - To remove a thread: `DELETE /threads/<thread_id>/`
    - To retrieve a list of threads for a user: `GET /threads_by_user/<user_id>`
    - To create a message: `POST /messages/`
    - To mark a message as read: `PUT /messages/<message_id>/read/`
    - To retrieve the number of unread messages for a user: `GET /unread/<user_id>`

3. You can use tools like URL or Postman to interact with the API endpoints.

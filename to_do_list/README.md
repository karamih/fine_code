# To-Do List App with Django and Docker

This is a simple To-Do List app built using Django and Django REST Framework (DRF). The app supports user authentication (login, registration) and task management (CRUD operations). It is Dockerized for easy setup and deployment.

## Features
- **User Authentication**: Register, login, and refresh JWT tokens.
- **Task Management**: Create, update, delete, and list tasks.
- **CRUD API**: All actions are performed via RESTful API endpoints.
- **Dockerized Setup**: The app is set up using Docker for easy deployment and development.

## Technologies
- **Backend**: Django, Django REST Framework, MySQL
- **Authentication**: JWT (JSON Web Tokens)
- **Containerization**: Docker

## Requirements
- Docker and Docker Compose
- Python 3.12+
- MySQL Database

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-repository/todo-app.git
cd todo-app
```

### 2. Create a `.env` file

Create a `.env` file in the root directory of the project and add the following environment variables:

```ini
DEBUG=1
DATABASE_NAME=admin_db
DATABASE_USER=admin
DATABASE_PASSWORD=admin
DATABASE_HOST=db
DATABASE_PORT=3306

MYSQL_DATABASE=admin_db
MYSQL_USER=admin
MYSQL_PASSWORD=admin
MYSQL_ROOT_PASSWORD=admin
```

### 3. Build and Run with Docker

Build and run the app using Docker Compose:

```bash
docker-compose up --build
```

This will:
- Build the Docker images for Django and MySQL.
- Start the Django app on `localhost:8000`.
- Start MySQL service on `localhost:3306`.

### 4. Apply Database Migrations

After the containers are up and running, you need to apply the database migrations:

```bash
docker-compose exec django python manage.py migrate
```

### 5. Create a Superuser (Optional)

If you want to create an admin user to manage the app, run:

```bash
docker-compose exec django python manage.py createsuperuser
```

## Testing

The app includes unit tests and integration tests for the authentication system and task management API.

### 1. Run Unit and Integration Tests

To run the unit tests and integration tests, use:

```bash
docker-compose exec django python manage.py test
```

This will execute all the tests for the app, including:

- Unit tests for individual components like task creation, user registration, etc.
- Integration tests for the API endpoints (e.g., creating a task via the API).

## Docker Compose Details

### `docker-compose.yml`

This file defines two services:

1. **django**: The Django app running on Python 3.12.
   - Exposes port `8000` on the host.
   - Depends on the `db` service.

2. **db**: The MySQL database service.
   - Exposes port `3306` on the host.
   - Uses environment variables from `.env` to set up the database.

### `Dockerfile`

The Dockerfile is used to build the Django app's image:

1. It starts from the official Python 3.12 image.
2. Installs dependencies from `requirements.txt`.
3. Copies the code into the container.

### `.env`

The `.env` file contains the necessary environment variables for the app, including database credentials and app configurations like `DEBUG`.

## Development

To make changes to the code:

1. Edit the files in your local development environment.
2. Restart the containers if necessary:

```bash
docker-compose restart
```

## API ENDPOINTS

All endpoints and usages are documented in this `postman` file: `fine_code.postman_collection.json`

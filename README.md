# Project Overview

This project contains two main components:

1. **Algorithm Directory**: A directory with Python code to solve algorithmic problems. This directory includes various algorithms, such as the `FindingPair` class that helps find pairs in a list that sum to a target value.
   
2. **Django To-Do App**: A web application built with Django that allows users to manage a to-do list. It includes features like user authentication (login, register, and refresh), task creation, and CRUD operations for tasks.

---

## Directory Structure

```bash
project/
│
├── algorithm/
│   ├── algorithm.py
│   └── ...
│
├── to_do_app/
│   ├── app/
│   ├── manage.py
│   ├── docker-compose.yml
│   └── ...
│
└── README.md
```

---

## Algorithm Directory

### Overview
The `algorithm` directory contains Python implementations of algorithms. The current implementation is for finding pairs of numbers from a list that sum up to a given target value.

### Key File: `algorithm.py`

- **Purpose**: The `FindingPair` class provides three different approaches to find a pair of numbers from a list that sum to a given target.
- **Approaches**:
  1. **Brute-force**: Iterates over each number in the list and checks for the complement.
  2. **Hash Set**: Uses a dictionary to store seen numbers, improving the time complexity to O(n).
  3. **Two-pointer**: Sorts the list and uses two pointers to find the pair.

#### Example Usage:
```python
numbers = [2, 5, 3, 8, 6, 11]
target = 8
finder = FindingPair(nums=numbers, target=target)

print(f'Approach One => pair with {target} as summation is: {finder.approach_one()}')
print(f'Approach Two => pair with {target} as summation is: {finder.approach_two()}')
print(f'Approach Three => pair with {target} as summation is: {finder.approach_three()}')
```

---

## Django To-Do App

### Overview
The `to_do_app` directory contains a Django-based application for managing tasks. It supports user authentication (register, login, and refresh JWT tokens) and allows users to create, retrieve, update, and delete tasks. The API is designed with Django REST Framework (DRF).

### Features
- **Authentication**: Register, login, and refresh JWT tokens for users.
- **Task Management**: Users can create tasks, mark them as completed, and retrieve or delete them.

### Key Files:
1. **`models.py`**: Contains the model for the `Task` object.
2. **`views.py`**: Defines the views for task management, including API views for creating, updating, and deleting tasks.
3. **`serializers.py`**: Defines the serializer for the `Task` model to convert data between JSON and Python objects.
4. **`urls.py`**: Configures URL routing for the task API endpoints.
5. **`tests/`**: Contains unit and integration tests for the task API.

#### Example Endpoints:
- **POST `/api/register/`**: Register a new user.
- **POST `/api/login/`**: Login a user and obtain a JWT token.
- **POST `/api/tasks/`**: Create a new task.
- **GET `/api/tasks/`**: Retrieve a list of tasks.
- **PUT `/api/tasks/<id>/`**: Update an existing task.
- **DELETE `/api/tasks/<id>/`**: Delete a task.

### Setup & Installation

#### Prerequisites:
- Docker
- Python 3.12+
- MySQL or another supported database

#### Installation Instructions:

1. **Clone the repository**:

   ```bash
   git clone <your-repository-url>
   cd <your-repository-folder>
   ```

2. **Set up environment variables**:
   - Create a `.env` file in the root directory (refer to `.env.example` for a template).
   
   Example `.env` file:
   ```
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

3. **Build and run the Docker containers**:

   ```bash
   docker-compose up --build
   ```

4. **Migrate the database**:
   Once the containers are up and running, execute migrations:

   ```bash
   docker-compose exec django python manage.py migrate
   ```

5. **Access the app**:
   - The Django app will be running on `http://localhost:8000/`.

---

## Running Tests

**Unit Tests**:
   - Unit tests for the Django app and algorithm directory are included. To run the tests for the Django app, use:

   ```bash
   docker-compose exec django python manage.py test
   ```
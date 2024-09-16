# 🚀 Isotec Backend API

## 📚 Table of Contents

- [User Guide](#user-guide)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
  - [API Endpoints](#api-endpoints)
- [Developer Guide](#developer-guide)
  - [Project Structure](#project-structure)
  - [Authentication Flow](#authentication-flow)
  - [Database Configuration](#database-configuration)
  - [Logging](#logging)
  - [Testing](#testing)

## 👤 User Guide

This section is aimed at users who want to run and use the API.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.7+
- Poetry (for dependency management) Install it here: https://python-poetry.org/docs/#installation

### Installation

1. Clone the repository:
   ```
   git clone git@github.com:luchog01/isotec-api-backend.git
   cd isotec-api-backend
   ```

2. Install dependencies using Poetry:
   ```
   poetry install
   ```

### Running the Application

1. Activate the Poetry virtual environment:
   ```
   poetry shell
   ```

2. Start the FastAPI server:
   ```
   uvicorn api.main:app
   ```

3. The API will be available at `http://localhost:8000`

### API Endpoints

- 🏠 `GET /`: Root endpoint
- 🔐 `POST /register`: Register a new user
- 🔑 `POST /token`: Login and receive an access token
- 👤 `GET /users/me`: Get current user information (requires authentication)

For detailed API documentation, visit `http://localhost:8000/docs` after starting the server.

## 🛠 Developer Guide

This section is for developers who want to understand and extend the FastAPI Auth App template.

### Project Structure

```
fastapi-auth-app/
├── api/
│   ├── controllers/
│   │   ├── auth.py
│   │   └── users.py
│   ├── data/
│   │   └── app.db
│   ├── exceptions/
│   │   └── custom_exceptions.py
│   ├── models/
│   │   └── user.py
│   ├── repositories/
│   │   ├── database.py
│   │   └── users.py
│   ├── routers/
│   │   ├── auth.py
│   │   └── users.py
│   ├── utils/
│   │   └── logger.py
│   └── main.py
├── logs/
│   └── api.log
├── tests/
├── .gitignore
├── README.md
└── pyproject.toml
```

### Authentication Flow

1. User registers via `/register` endpoint
2. User logs in via `/token` endpoint, receives a JWT
3. JWT is used in the `Authorization` header for authenticated requests

### Database Configuration

- SQLite database located at `api/data/app.db`
- Configured in `api/repositories/database.py`
- Uses SQLAlchemy for ORM

### Logging

- Application logs: `logs/api.log`
- Configured in `api/utils/logger.py`

### Testing

1. Write tests in the `tests/` directory
2. Run tests using pytest:
   ```
   poetry run pytest
   ```

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgements

- FastAPI
- SQLAlchemy
- Pydantic
- Poetry

Happy coding! 🎉

# FastAPI JWT Authentication

A robust JWT (JSON Web Token) authentication system built with FastAPI, providing secure user registration, login, and protected routes.

## Features

- User registration with email validation
- Secure password hashing using bcrypt
- JWT-based authentication
- Access and refresh token system
- Protected routes using JWT
- SQLAlchemy integration with SQLite database
- Modern Python type hints and Pydantic models

## Project Structure
```
FastAPIv1/
├── app/
│   ├── __init__.py
│   ├── app.py            # Main FastAPI application
│   ├── database/
│   │   ├── __init__.py
│   │   └── db.py        # Database configuration
│   ├── models.py         # SQLAlchemy models
│   ├── schemas.py        # Pydantic models/schemas
│   ├── deps.py          # Dependencies (auth, etc.)
│   └── utils.py         # Utility functions
└── requirements.txt
```

## Requirements

- Python 3.13+
- Dependencies listed in requirements.txt:
  - fastapi>=0.100.0
  - pydantic[email]>=2.0.0
  - uvicorn>=0.15.0
  - python-jose[cryptography]>=3.3.0
  - passlib[bcrypt]>=1.7.4
  - python-multipart>=0.0.5
  - sqlalchemy>=1.4.23
  - python-dotenv>=0.19.0
  - bcrypt>=4.0.1
  - email-validator>=2.0.0

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd fastapi-jwt-auth
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the server:
```bash
uvicorn app.app:app --reload
```

2. Access the API documentation:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## API Endpoints

### Authentication

#### POST /signup
Register a new user
```json
{
    "email": "user@example.com",
    "username": "username",
    "password": "secretpassword"
}
```

#### POST /login
Login and receive access & refresh tokens
```json
{
    "username": "user@example.com",
    "password": "secretpassword"
}
```

#### GET /me
Get current user information (Protected route)
- Requires Bearer token authentication

## Authentication Flow

1. **Registration**: Users register with email, username, and password
2. **Login**: Users receive access and refresh tokens upon successful login
3. **Protected Routes**: Access token is used to authenticate requests
4. **Token Refresh**: Refresh token can be used to obtain new access tokens

## Security Features

- Passwords are hashed using bcrypt
- JWT tokens with expiration
- Email validation
- SQL injection protection through SQLAlchemy
- Type validation using Pydantic
- Protected routes using FastAPI dependencies

## Database

The project uses SQLite as the database, configured in `app/database/db.py`. The database file `app.db` is created automatically when the application first runs.

### Models

#### User Model
```python
class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String)
    password = Column(String)
```

## Environment Variables

Create a `.env` file in the root directory with:
```env
JWT_SECRET_KEY=your-super-secret-key
JWT_REFRESH_SECRET_KEY=your-refresh-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_MINUTES=10080  # 7 days
```

## Development

To contribute to this project:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## Testing

Run tests using pytest:
```bash
pytest
```

## Common Issues and Solutions

1. **ModuleNotFoundError**: Make sure you're running the application from the correct directory and the virtual environment is activated.

2. **Database Errors**: If you encounter database issues, try deleting the `app.db` file and restarting the application.

3. **Email Validation Errors**: Ensure email-validator is installed: `pip install email-validator`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

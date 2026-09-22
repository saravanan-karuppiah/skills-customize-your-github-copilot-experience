# 📘 Assignment: Secure a FastAPI API with Authentication

## 🎯 Objective

Extend a FastAPI book API with user authentication and protected routes. You will practice password hashing, login validation, bearer tokens, and authorization while keeping user data in memory for a focused advanced exercise.

## 📝 Tasks

### 🛠️ Implement User Authentication

#### Description

Complete the authentication helpers and login route in `starter-code.py`. Users should be able to submit credentials and receive a bearer token only when the credentials are valid.

#### Requirements

Completed program should:

- Hash passwords with the provided PBKDF2 helper and never store a plain-text password in the user records.
- Implement `verify_password` so it safely compares a submitted password with the stored password hash.
- Complete `POST /token` so valid credentials return an access token and invalid credentials return status code `401` with a `WWW-Authenticate: Bearer` header.

### 🛠️ Protect the Book API

#### Description

Use the bearer token dependency to restrict access to the book routes and identify the authenticated user.

#### Requirements

Completed program should:

- Implement `get_current_user` so missing, malformed, or unknown tokens produce status code `401`.
- Require authentication for `GET /books` and `POST /books` while preserving the existing book behavior for authorized requests.
- Verify the workflow at `/docs`: log in with the sample user, authorize with the returned token, confirm authorized requests succeed, and confirm requests without a token fail.

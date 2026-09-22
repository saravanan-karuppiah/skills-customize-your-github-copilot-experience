# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI that manages a collection of books. You will practice defining routes, validating JSON request data with Pydantic models, returning appropriate HTTP responses, and running an API locally with automatic documentation.

## 📝 Tasks

### 🛠️ Create the Book API

#### Description

Complete the starter application so clients can list books, retrieve one book by ID, and add a new book.

#### Requirements

Completed program should:

- Start a FastAPI application from `starter-code.py` and expose a `GET /books` endpoint that returns all books as JSON.
- Expose a `GET /books/{book_id}` endpoint that returns one book when the ID exists and a `404` response when it does not.
- Define a Pydantic request model and expose a `POST /books` endpoint that validates the title and author, creates a book with a unique ID, and returns a `201` response.

### 🛠️ Test and Document the API

#### Description

Run the API locally and use FastAPI's generated documentation to check each route and response.

#### Requirements

Completed program should:

- Run with `uvicorn starter-code:app --reload` and show no startup errors.
- Verify successful `GET` and `POST` requests using the interactive documentation at `/docs`.
- Verify that an unknown book ID returns status code `404` and that invalid book data is rejected with status code `422`.

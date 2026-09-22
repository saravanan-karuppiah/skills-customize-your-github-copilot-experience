import base64
import hashlib
import hmac
import secrets
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

app = FastAPI(title="Secure Book API")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class BookCreate(BaseModel):
    title: str
    author: str


def hash_password(password: str, salt: bytes | None = None) -> str:
    """Return a portable PBKDF2 password hash."""
    salt = salt or secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100_000)
    return f"{base64.b64encode(salt).decode()}${base64.b64encode(digest).decode()}"


def verify_password(password: str, stored_hash: str) -> bool:
    """Check a password against a hash returned by hash_password."""
    # TODO: Decode the salt and digest, hash the submitted password, and compare safely.
    return False


users = {
    "student": {
        "username": "student",
        "password_hash": hash_password("learn-fastapi"),
    }
}

# This demo token store is intentionally in memory.
tokens = {}
books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
]


@app.post("/token")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """Validate credentials and return a bearer token."""
    # TODO: Look up the user, verify the password, create a token, and store its owner.
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    """Return the user associated with a bearer token."""
    # TODO: Look up the token and reject unknown tokens with a 401 response.
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},
    )


@app.get("/books")
def list_books(current_user: Annotated[dict, Depends(get_current_user)]):
    """Return all books to an authenticated user."""
    return books


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(
    book: BookCreate,
    current_user: Annotated[dict, Depends(get_current_user)],
):
    """Create a book for an authenticated user."""
    new_book = {"id": len(books) + 1, **book.model_dump()}
    books.append(new_book)
    return new_book

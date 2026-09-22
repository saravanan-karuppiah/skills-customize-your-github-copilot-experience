from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Book API")


class BookCreate(BaseModel):
    title: str
    author: str


books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
]


@app.get("/books")
def list_books():
    """Return all books."""
    # TODO: Return the books collection.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    """Return one book or a 404 response."""
    # TODO: Find the requested book and raise HTTPException when it is missing.
    pass


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    """Create and return a new book."""
    # TODO: Create a unique ID, append the new book, and return it.
    pass

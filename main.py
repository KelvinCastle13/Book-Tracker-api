from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from models import Book

app = FastAPI()

books: List[Book] = []

books: List[Book] = [
    Book(id=1, title="1984", author="George Orwell", genre="Dystopian"),
    Book(id=2, title="The Catcher in the Rye", author="J.D. Salinger", genre="Fiction"),
    Book(id=3, title="To Kill a Mockingbird", author="Harper Lee", genre="Classic"),
]

@app.get("/", response_model=List[Book])
def read_root():
  return books

@app.post("/books/", response_model=Book)
def create_book(book: Book):
  book.append(book)
  return book

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
  for book in books:
    if book.id == book_id:
      return book
  raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
  for i, book in enumerate(books):
    if book.id == book_id:
        books[i] = updated_book
        return update_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/book/{book_id}")
def delete_book(book_id: int):
  for i, book in enumerate(bookd):
    if book.id == book_id:
      books.pop(i)
      return {"message": "Book delted"}
      raise HTTPException(status_code=404, detail="Book not found")

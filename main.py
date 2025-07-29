from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from models import Book, BookCreate
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["http://localhost:4200"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

books: List[Book] = [
    Book(id=1, title="1984", author="George Orwell", genre="Dystopian", status=True),
    Book(id=2, title="The Catcher in the Rye", author="J.D. Salinger", genre="Fiction", status=False),
    Book(id=3, title="To Kill a Mockingbird", author="Harper Lee", genre="Classic", status=False),
    Book(id=4, title="Brave New World", author="Aldous Huxley", genre="Dystopian", status=False),
    Book(id=5, title="The Great Gatsby", author="F. Scott Fitzgerald", genre="Classic", status=False),
    Book(id=6, title="Moby-Dick", author="Herman Melville", genre="Adventure", status=False),
    Book(id=7, title="Pride and Prejudice", author="Jane Austen", genre="Romance", status=False),
    Book(id=8, title="The Hobbit", author="J.R.R. Tolkien", genre="Fantasy", status=False),
    Book(id=9, title="Fahrenheit 451", author="Ray Bradbury", genre="Science Fiction", status=False),
    Book(id=10, title="Jane Eyre", author="Charlotte Brontë", genre="Gothic", status=False),
    Book(id=11, title="Slaughterhouse-Five", author="Kurt Vonnegut", genre="Satire", status=False),
    Book(id=12, title="Crime and Punishment", author="Fyodor Dostoevsky", genre="Philosophical", status=False),
    Book(id=13, title="The Road", author="Cormac McCarthy", genre="Post-apocalyptic", status=False),
]

@app.get("/", response_model=List[Book])
def read_root():
  return books

@app.post("/books/", response_model=Book)
def create_book(book: BookCreate):
  new_id = max((b.id for b in books), default=0) + 1
  new_book = Book(id=new_id, **book.dict())
  books.append(new_book)
  return new_book

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
        return updated_book
  raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
  for i, book in enumerate(books):
    if book.id == book_id:
      books.pop(i)
      return {"message": "Book delted"}
  raise HTTPException(status_code=404, detail="Book not found")

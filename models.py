from pydantic import BaseModel
from typing import Optional

class BookBase(BaseModel):
  title: str
  author: str
  genre: str
  status: bool = False

class BookCreate(BookBase):
  pass

class Book(BookBase):
  id: int
from typing import List, Optional
from pydantic import BaseModel, EmailStr, Field

# Пользователь

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(..., min_length=4)

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# Автор

class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True

# Книга

class BookBase(BaseModel):
    title: str
    author_id: int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    author: Optional[Author] = None

    class Config:
        orm_mode = True

# Отзыв

class ReviewBase(BaseModel):
    rating: float = Field(..., ge=0, le=5)
    text: Optional[str] = None
    book_id: int

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

# Токен

class Token(BaseModel):
    access_token: str
    token_type: str

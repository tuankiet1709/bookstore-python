from datetime import datetime
from uuid import UUID
from schemas.book import Book
from models.book import BookModel, BookPaginationModel, BookViewModel
from database import get_db_context
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, Query


def http_exception(code: int, message: str):
    return HTTPException(status_code=code, tags=["Books"], detail=message)


class BookService:
    def __init__(self, db: Session = Depends(get_db_context)):
        self._db = db

    async def get_all_book(self) -> [BookViewModel]:
        return self._db.query(Book).all()
    
    async def get_book_pagination(self, book_pagination: BookPaginationModel) -> [BookViewModel]:
        query = self._db.query(Book)
        
        if book_pagination.title is not None:
            query = query.filter(Book.title.like(f'{book_pagination.title}%'))
        
        if book_pagination.author_id is not None:
            query = query.filter(Book.author_id == book_pagination.author_id)
            
        return query.offset((book_pagination.page-1)*book_pagination.size).limit(book_pagination.size).all()

    async def get_book_by_id(self, id: UUID) -> BookViewModel:
        book = self._db.query(Book).filter(Book.id == id).first()
        if book is None:
            raise http_exception(401, f"There are no book have id = {id}")
        return book

    async def create_book(self, book_create_request: BookModel) -> None:
        try:
            book = Book(**book_create_request.dict())
            book.created_at = datetime.utcnow()

            self._db.add(book)
            self._db.commit()
        except Exception as e:
            raise http_exception(400, e)
    
    async def update_book(self, id: UUID, book_update_request: BookModel) -> BookModel:
        book = self._db.query(Book).filter(Book.id == id).first()
        if book is None:
            raise http_exception(401, f"There are no book have id = {id}")
        
        book.title = book_update_request.title
        book.description = book_update_request.description
        book.mode = book_update_request.mode
        book.rating = book_update_request.rating
        book.author_id = book_update_request.author_id
        book.update_at = datetime.utcnow()
        
        self._db.add(book)
        self._db.commit()
        return book
    
    async def remove_book(self, id: UUID) -> None:
        book = self._db.query(Book).filter(Book.id == id).first()
        if book is None:
            raise http_exception(401, f"There are no book have id = {id}")

        self._db.delete(book)
        self._db.commit()
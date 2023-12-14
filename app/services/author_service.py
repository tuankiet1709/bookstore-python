from datetime import datetime
from uuid import UUID
from schemas.author import Author
from database import get_db_context
from sqlalchemy.orm import Session
from models.author import AuthorModel, AuthorViewModel
from fastapi import Depends, HTTPException


def http_exception(code: int, message: str):
    return HTTPException(status_code=code, tags=["Authors"], detail=message)


class AuthorService:
    def __init__(self, db: Session = Depends(get_db_context)):
        self._db = db

    async def get_all_author(self) -> [AuthorViewModel]:
        try:
            return self._db.query(Author).all()
        except Exception as e:
            print(e)

    async def get_author_by_id(self, id: UUID) -> AuthorViewModel:
        author = self._db.query(Author).filter(Author.id == id).first()
        if author is not None:
            return author
        raise http_exception(401, f"There are no author have id = {id}")

    async def create_author(self, author_create_request: AuthorModel) -> None:
        try:
            author = Author(**author_create_request.dict())
            author.created_at = datetime.utcnow()

            self._db.add(author)
            self._db.commit()
        except Exception as e:
            raise http_exception(400, e)
    
    async def update_author(self, id: UUID, author_update_request: AuthorModel) -> AuthorModel:
        author = self._db.query(Author).filter(Author.id == id).first()
        if author is None:
            raise http_exception(401, f"There are no author have id = {id}")
        
        author.full_name = author_update_request.full_name
        author.gender = author_update_request.gender
        author.update_at = datetime.utcnow()
        
        self._db.add(author)
        self._db.commit()
        return author
    
    async def remove_author(self, id: UUID) -> None:
        author = self._db.query(Author).filter(Author.id == id).first()
        if author is None:
            raise http_exception(401, f"There are no author have id = {id}")

        self._db.delete(author)
        self._db.commit()

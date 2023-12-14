from datetime import datetime
from typing import Optional
from uuid import UUID
from models.author import AuthorViewModel
from schemas.base_entity import BookMode
from pydantic import BaseModel, Field
from fastapi import Query


class BookModel(BaseModel):
    title: str = Field(min_length=1)
    description: str = Field(min_length=1)
    mode: BookMode = Field(default=BookMode.DRAFT)
    rating: int = Field(ge=0, le=5, default=0)
    author_id: UUID


class BookPaginationModel(BaseModel):
    title: Optional[str] = Query(default=None)
    author_id: Optional[UUID] = Query(default=None)
    page: int = Query(gt=0, default=1)
    size: int = Query(gt=0, le=50, default=10)


class BookViewModel(BaseModel):
    id: UUID
    title: str
    description: str
    mode: BookMode
    rating: int
    author_id: UUID
    author: AuthorViewModel
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        from_attributes = True


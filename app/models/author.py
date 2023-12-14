from datetime import datetime
from uuid import UUID
from schemas.base_entity import Gender
from pydantic import BaseModel, Field


class AuthorModel(BaseModel):
    full_name: str = Field(min_length=1)
    gender: Gender = Field(default=Gender.NONE)


class AuthorViewModel(BaseModel):
    id: UUID
    full_name: str
    gender: str
    created_at: datetime | None = None

    class Config:
        from_attributes = True

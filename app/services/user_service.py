from fastapi import Depends
from schemas.user import User
from models.user import UserViewModel
from database import SessionLocal, get_db_context
from sqlalchemy.orm import Session


class UserService:
    def __init__(self, db: Session = Depends(get_db_context)):
        self._db = db

    async def get_users(self) -> [UserViewModel]:
        return self._db.query(User).filter(User.is_active == True).all()
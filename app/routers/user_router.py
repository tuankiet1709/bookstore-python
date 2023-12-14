from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controllers.user_controller import UserController

from database import get_db_context
from schemas.user import User
from models.user import UserViewModel

router = APIRouter(prefix="/users", tags=["User"])


@router.get("", response_model=List[UserViewModel])
async def get_users(
    user_controller: UserController = Depends(UserController),
) -> List[UserViewModel]:
    return await user_controller.get_all_user()

from fastapi import Depends

from models.user import UserViewModel
from services.user_service import UserService


class UserController:
    def __init__(self, user_service: UserService = Depends(UserService)):
        self._user_service = user_service
    
    async def get_all_user(self) -> [UserViewModel]:
        return await self._user_service.get_users()
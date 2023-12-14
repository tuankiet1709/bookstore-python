from datetime import datetime
from uuid import UUID
from models.author import AuthorViewModel, AuthorModel
from services.author_service import AuthorService
from fastapi import Depends


class AuthorController:
    def __init__(self, authorService: AuthorService = Depends(AuthorService)):
        self._authorService = authorService

    async def get_all_author(self) -> [AuthorViewModel]:
        return await self._authorService.get_all_author()

    async def get_author_by_id(self, id: UUID) -> AuthorViewModel:
        return await self._authorService.get_author_by_id(id)

    async def create_author(self, request: AuthorModel) -> None:
        await self._authorService.create_author(request)

    async def update_author(self, id: UUID, update_request: AuthorModel) -> AuthorModel:
        return await self._authorService.update_author(id, update_request)

    async def remove_author(self, id: UUID) -> None:
        await self._authorService.remove_author(id)

from uuid import UUID
from models.book import BookModel, BookPaginationModel, BookViewModel
from services.book_service import BookService
from fastapi import Depends


class BookController:
    def __init__(self, bookService: BookService = Depends(BookService)):
        self._bookService = bookService
    
    async def get_all_book(self) -> [BookViewModel]:
        return await self._bookService.get_all_book()
    
    async def get_book_pagination(self, book_pagination: BookPaginationModel) -> [BookViewModel]:
        return await self._bookService.get_book_pagination(book_pagination)
    
    async def get_book_by_id(self, id: UUID) -> BookViewModel:
        return await self._bookService.get_book_by_id(id)
    
    async def create_book(self, request: BookModel) -> None:
        await self._bookService.create_book(request)
        
    async def update_book(self, id: UUID, update_request: BookModel) -> BookModel:
        return await self._bookService.update_book(id, update_request)
    
    async def remove_book(self, id: UUID) -> None:
        await self._bookService.remove_book(id)
        
        
from uuid import UUID
from controllers.book_controller import BookController
from models.book import BookModel, BookPaginationModel, BookViewModel
from fastapi import Depends, APIRouter, Query
from starlette import status
from services.auth_service import token_interceptor
from schemas.user import User

router = APIRouter(prefix="/books", tags=["Book"])

@router.get("", response_model=list[BookViewModel])
async def get_all_book(bookController: BookController = Depends(BookController), token: User = Depends(dependency=token_interceptor)):
    return await bookController.get_all_book()

@router.get("/pagination", response_model=list[BookViewModel])
async def get_book_pagination(
    book_pagination: BookPaginationModel = Depends(),
    bookController: BookController = Depends(BookController)):
    return await bookController.get_book_pagination(book_pagination)

@router.get("/{id}", response_model=BookViewModel)
async def get_book_by_id(id: UUID, bookController: BookController = Depends(BookController)):
    return await bookController.get_book_by_id(id)

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_book(request: BookModel, bookController: BookController = Depends(BookController)):
    await bookController.create_book(request)
    
@router.put("/{id}", response_model=BookModel)
async def update_book(id: UUID, update_request: BookModel, bookController: BookController = Depends(BookController)) -> BookModel:
    return await bookController.update_book(id, update_request)

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def remove_book(id: UUID, bookController: BookController = Depends(BookController)):
    await bookController.remove_book(id)
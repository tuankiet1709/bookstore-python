from uuid import UUID
from models.author import AuthorModel, AuthorViewModel
from fastapi import Depends, APIRouter
from starlette import status
from controllers.author_controller import AuthorController


router = APIRouter(prefix="/authors", tags=["Author"])

@router.get("", response_model=list[AuthorViewModel])
async def get_all_author(authorController: AuthorController = Depends(AuthorController)):
    return await authorController.get_all_author()

@router.get("/{id}", response_model=AuthorViewModel)
async def get_author_by_id(id: UUID, authorController: AuthorController = Depends(AuthorController)):
    return await authorController.get_author_by_id(id)

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_author(request: AuthorModel, authorController: AuthorController = Depends(AuthorController)):
    await authorController.create_author(request)
    
@router.put("/{id}", response_model=AuthorModel)
async def update_author(id: UUID, update_request: AuthorModel, authorController: AuthorController = Depends(AuthorController)) -> AuthorModel:
    return await authorController.update_author(id, update_request)

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def remove_author(id: UUID, authorController: AuthorController = Depends(AuthorController)):
    await authorController.remove_author(id)
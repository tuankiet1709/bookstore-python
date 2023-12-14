from datetime import timedelta
from services import auth_service
from database import get_db_context
from fastapi import Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db_context)):
    user = auth_service.authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise auth_service.token_exception()
    return {
        "access_token": auth_service.create_access_token(user, timedelta(minutes=60)),
        "token_type": "bearer"
    }
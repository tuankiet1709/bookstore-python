from datetime import datetime, timedelta
from uuid import UUID
from settings import JWT_ALGORITHM, JWT_SECRET
from schemas import User, verify_password
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from typing import Optional
from jose import jwt, JWTError
from sqlalchemy.orm import Session

oa2_bearer = OAuth2PasswordBearer(tokenUrl="/auth/token")

def create_access_token(user: User, expires: Optional[timedelta] = None) -> str:
    claims = {
        "sub": user.username,
        "id": str(user.id),
        "last_name": user.last_name,
        "first_name": user.first_name,
        "is_admin": user.is_admin,
    }

    expire = (
        datetime.utcnow() + expires
        if expires
        else datetime.utcnow() + timedelta(minutes=60)
    )
    claims.update({"exp": expire})
    return jwt.encode(claims, JWT_SECRET, algorithm=JWT_ALGORITHM)


def authenticate_user(username: str, password: str, db: Session):
    user: User = db.query(User).filter(User.username == username).first()

    if not User:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def token_interceptor(token: str = Depends(oa2_bearer)) -> User:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])

        user: User = User()
        user.username = payload.get("sub")
        user.id = UUID(payload.get("id"))
        user.first_name = payload.get("first_name")
        user.last_name = payload.get("last_name")
        user.is_admin = payload.get("is_admin")

        if user.username is None or user.id is None:
            raise token_exception()
        return user
    except JWTError:
        raise token_exception()


def token_exception():
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="username/password is incorrect",
        headers={"WWW-Authenticate": "Bearer"},
    )

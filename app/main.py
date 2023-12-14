from fastapi import FastAPI
from routers import author_router, book_router, user_router, auth_router

app = FastAPI()

app.include_router(author_router.router)
app.include_router(book_router.router)
app.include_router(user_router.router)
app.include_router(auth_router.router)
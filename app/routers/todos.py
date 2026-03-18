from fastapi import Request
from app.dependencies import SessionDep
from app.dependencies.auth import AuthDep
from sqlmodel import select
from app.models.todo import Todo
from . import api_router

@api_router.get("/todos")
async def list_todos(user: AuthDep, db: SessionDep):
    return db.exec(select(Todo).where(Todo.user_id == user.id)).all()
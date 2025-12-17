from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from ..db import get_session
from ..models.user import User

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/")
async def create_user(
    user: User,
    session: Annotated[AsyncSession, Depends(get_session)],
) -> User:
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user

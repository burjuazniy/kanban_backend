from typing import Annotated, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
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


@router.get("/")
async def list_users(
    session: Annotated[AsyncSession, Depends(get_session)]
) -> List[User]:
    result = await session.execute(select(User))
    return list(result.scalars().all())


@router.get("/{user_id}")
async def get_user(
    user_id: int,
    session: Annotated[AsyncSession, Depends(get_session)],
) -> User:
    result = await session.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

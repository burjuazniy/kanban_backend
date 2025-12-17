from typing import Annotated
from fastapi import APIRouter, Depends
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from ..db import get_session
from ..models.task import Task

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/")
async def create_task(
    task: Task,
    session: Annotated[AsyncSession, Depends(get_session)],
) -> Task:
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task


@router.get("/")
async def list_tasks(session: Annotated[AsyncSession, Depends(get_session)]) -> list[Task]:
    result = await session.execute(select(Task))
    return [x for x in result.scalars().all()]

from sqlmodel import SQLModel, Field, Relationship

class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    user_id: int = Field(foreign_key="user.id")

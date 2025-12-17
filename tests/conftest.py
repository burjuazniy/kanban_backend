import os
import asyncio
import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel

from src.kanban_backend.main import app
from src.kanban_backend.db import engine, init_db


@pytest.fixture(scope="session", autouse=True)
def prepare_database():
    asyncio.run(init_db(database_url='sqlite+aiosqlite:///./test_db.sqlite3'))
    yield
    os.remove('./test_db.sqlite3')


@pytest.fixture()
def client():
    return TestClient(app)

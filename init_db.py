import asyncio
from src.kanban_backend.db import init_db

if __name__ == "__main__":
    asyncio.run(init_db())

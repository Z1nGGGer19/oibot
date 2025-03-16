from .db import async_session
from .models import Task, User

from sqlalchemy.future import select

async def add_user(id):
    async with async_session() as session:
        user = User(user_id=id)
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user
    
async def get_user(id):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.user_id == id))
        user = result.scalar_one_or_none()
        if not user:
            await add_user(id)

async def get_task_count() -> int:
    async with async_session() as session:
        result = await session.execute(select(Task))
        count = result.scalar_one_or_none()
        return count

async def get_users():
    async with async_session() as session:
        result = await session.execute(select(User))
        return result.scalars().all()
    
async def add_task(value: int):
    async with async_session() as session:
        new_task = Task(value=value)
        session.add(new_task)
        await session.commit()
        await session.refresh(new_task)
        return new_task


async def get_task():
    async with async_session() as session:
        result = await session.execute(select(Task))
        task = result.scalars().first()
        return task.value
    

async def update_first_task_value(new_value: int):
    async with async_session() as session:
        result = await session.execute(select(Task))
        task = result.scalars().first()
    
        if task:
            task.value = new_value
            await session.commit()
            return task
        else:
            raise ValueError("Таблица tasks пуста.")
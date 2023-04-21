from asyncpg.exceptions import UniqueViolationError
import logging
from typing import Any

class Database:

    def __init__(self, pool):
        self.pool = pool

    async def create_user(self, user_id: int):
        async with self.pool.acquire() as conn:
            try:
                await conn.execute("insert into users(user_id) values($1)", user_id)
            except UniqueViolationError:
                logging.error("User already exist")

    async def fetch_questions(self) -> list:
        async with self.pool.acquire() as conn:
            result = await conn.fetch("select * from entrant_questions")
            return result

    async def fetch_clubs(self) -> list:
        async with self.pool.acquire() as conn:
            result = await conn.fetch("select * from clubs")
            return result

    async def fetch_club_info(self, club_name: str) -> list:
        async with self.pool.acquire() as conn:
            result = await conn.fetch("select * from clubs where name = $1", club_name)
            return result[0]

    async def fetch_question_info_by_id(self, question_id: int) -> list:
        async with self.pool.acquire() as conn:
            result = await conn.fetch("select * from entrant_questions where id = $1", question_id)
            return result[0]


from typing import Optional, Tuple

import sqlmodel as sm
from loguru import logger

from .db import engine


class Hero(sm.SQLModel, table=True):
    id: Optional[int] = sm.Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int]


def output(prefix: str, heros: Tuple[Hero]) -> None:
    logger.debug(f"{prefix}: {heros=}")


def create_rows() -> None:
    hero1 = Hero(name="hero1", secret_name="c2io")
    hero2 = Hero(name="hero2", secret_name="c2io2")

    with sm.Session(engine) as s:
        s.add(hero1)
        s.add(hero2)

        prefix = "before commit"
        output(prefix, (hero1, hero2))

        s.commit()

        prefix = "after commit"
        output(prefix, (hero1, hero2))

        _ = hero1.name
        s.refresh(hero2)

        prefix = "after access attr or refresh"
        output(prefix, (hero1, hero2))


def create_tables():
    sm.SQLModel.metadata.create_all(engine)


def main():
    create_tables()
    create_rows()


if __name__ == "__main__":
    main()

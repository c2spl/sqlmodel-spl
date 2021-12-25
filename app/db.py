from pathlib import Path

import sqlmodel as sm

sqlite_filename = "data/database.sqlite3"
database_url = f"sqlite:///{sqlite_filename}"

Path(sqlite_filename).unlink(missing_ok=True)

engine = sm.create_engine(database_url, echo=False)


def create_db_and_tables():
    sm.SQLModel.metadata.create_all(engine)

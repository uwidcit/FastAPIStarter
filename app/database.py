from contextlib import contextmanager
from sqlmodel import Session, SQLModel, create_engine
from typing import Annotated
from fastapi import Depends
from app.models import *
from app.settings import get_settings



engine = create_engine(get_settings().database_uri, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def drop_all():
    SQLModel.metadata.drop_all(bind=engine)

def _session_generator():
    with Session(engine) as session:
        yield session

def get_session():
    yield from _session_generator()

@contextmanager
def get_cli_session():
    yield from _session_generator()


SessionDep = Annotated[Session, Depends(get_session)]
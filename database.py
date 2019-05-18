from sqlalchemy import create_engine

from app_config import db_connection

engine = create_engine(db_connection, echo=True)

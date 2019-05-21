import os

from sqlalchemy import create_engine, MetaData

engine = create_engine(os.environ['DB_CONNECTION'], echo=True)
metadata = MetaData()

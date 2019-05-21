from sqlalchemy import Table

from data.connection import engine, metadata

client_table = Table('client', metadata, autoload=True, autoload_with=engine)
token_table = Table('token', metadata, autoload=True, autoload_with=engine)

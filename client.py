import os
import random
import string
from datetime import datetime, timedelta

import jwt
from sqlalchemy import select

from data import engine, client_table
from data.tables import token_table
from hash import get_hashed_password, check_password

jwt_secret = os.environ['JWT_SECRET']


def random_string(str_length):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    result = ''

    for i in range(str_length):
        result += random.choice(letters)

    return result


def encode(payload):
    return jwt.encode(payload, jwt_secret, algorithm='HS256').decode('utf-8')


class NotFoundException(Exception):
    pass


def map_row_to_client(row):
    return Client(
        client_id=row['client_id'],
        email=row['email'],
        password_hash=row['password_hash'],
        name=row['name']
    )


def fetch_client(whereclause):
    result = engine.execute(select([client_table]).where(whereclause).limit(1))

    row = result.fetchone()
    result.close()

    if row is None:
        raise NotFoundException()

    return map_row_to_client(row)


def create_client(email, password, name):
    password_hash = get_hashed_password(password)

    result = engine.execute(client_table.insert().values(email=email, password_hash=password_hash, name=name))
    client_id = result.inserted_primary_key[0]
    result.close()

    return find_client_with_id(client_id)


def find_client_with_id(client_id):
    return fetch_client(client_table.c.client_id == client_id)


def find_client_with_email(email):
    return fetch_client(client_table.c.email == email)


def create_token(client):
    client_id = client.client_id
    time = datetime.utcnow()
    access_token = encode({
        'client_id': client_id,
        'email': client.email,
        'name': client.name,
        'token_creation': str(time)
    })
    refresh_token = random_string(50)
    access_expired = time + timedelta(minutes=15)
    refresh_expired = time + timedelta(days=1)

    engine.execute(token_table.insert().values(token=refresh_token, client_id=client_id, expired_at=refresh_expired))

    return {
        'access_token': access_token,
        'refresh_token': refresh_token,
        'expired_at': str(access_expired)
    }


def update_token(refresh_token):
    result = engine.execute(
        token_table.delete().where(token_table.c.token == refresh_token).returning(
            token_table.c.expired_at, token_table.c.client_id)
    )

    row = result.fetchone()

    if row is None:
        raise Exception()

    client_id = row['client_id']
    expired_at = row['expired_at']

    if expired_at < datetime.utcnow():
        raise Exception()

    return create_token(find_client_with_id(client_id))


class Client(object):
    def __init__(self, client_id, email, password_hash, name):
        self.client_id = client_id
        self.email = email
        self.password_hash = password_hash
        self.name = name

    def verify_password(self, password):
        return check_password(password, self.password_hash)

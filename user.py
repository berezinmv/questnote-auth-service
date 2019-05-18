from hash import get_hashed_password, check_password


def create_user(email, password, name):
    password_hash = get_hashed_password(password)

    # todo create user in database

    user_id = None

    return User(
        user_id=user_id,
        email=email,
        password_hash=password_hash,
        name=name
    )


def find_user_with_email(email):
    # todo find user in database

    user_id = None
    password_hash = ''
    name = ''

    return User(
        user_id=user_id,
        email=email,
        password_hash=password_hash,
        name=name
    )


def get_user(user_id):
    # todo find user in database

    email = ''
    password_hash = ''
    name = ''

    return User(
        user_id=user_id,
        email=email,
        password_hash=password_hash,
        name=name
    )


class User(object):
    def __init__(self, user_id, email, password_hash, name):
        self.user_id = user_id
        self.email = email
        self.password_hash = password_hash
        self.name = name

    def verify_password(self, password):
        return check_password(password, self.password_hash)

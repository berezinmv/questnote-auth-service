from passlib.hash import sha256_crypt


def get_hashed_password(password):
    return sha256_crypt.encrypt(password)


def check_password(password, hashed_password):
    return sha256_crypt.verify(password, hashed_password)

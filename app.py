from flask import Flask, jsonify

from serialize import serialize_user
from user import User

app = Flask(__name__)
user = User(
    user_id=23,
    email='test@ggg.com',
    password_hash='131231231231asasd',
    name='Maxim Berezin'
)


@app.route('/api/v1/authenticate')
def authenticate():
    return jsonify(serialize_user(user))


@app.route('/api/v1/get_user')
def get_user():
    return jsonify(serialize_user(user))


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

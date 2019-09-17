from flask import Flask, request, jsonify

from client import create_client, find_client_with_email, create_token, update_token, NotFoundException

app = Flask(__name__)


@app.route('/api/v1/register', methods=['POST'])
def register():
    args = request.get_json()
    email = args.get('email')
    password = args.get('password')
    name = args.get('name', '')

    client = create_client(email=email, password=password, name=name)

    return jsonify(create_token(client))


@app.route('/api/v1/authenticate', methods=['POST'])
def authenticate():
    args = request.get_json()
    email = args.get('email')
    password = args.get('password')

    try:
        client = find_client_with_email(email)

        if client.verify_password(password):
            return jsonify(create_token(client))
    except NotFoundException:
        return jsonify({'message': 'client not found'})

    return jsonify({'message': 'client not found'})


@app.route('/api/v1/refresh', methods=['POST'])
def refresh():
    args = request.get_json()
    refresh_token = args.get('refresh_token')

    return jsonify(update_token(refresh_token))


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')

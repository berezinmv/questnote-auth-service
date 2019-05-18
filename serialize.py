def serialize_user(user):
    return {
        'user_id': user.user_id,
        'email': user.email,
        'name': user.name
    }

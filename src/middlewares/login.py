from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask import jsonify, request
from functools import wraps

def me_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            user = get_jwt()
            user_id = request.view_args['user_id']
            
            if user_id and user["sub"] == user_id:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="User only!"), 403

        return decorator

    return wrapper

def admin_required():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["is_administrator"]:
                return fn(*args, **kwargs)
            else:
                return jsonify(msg="Admins only!"), 403

        return decorator

    return wrapper

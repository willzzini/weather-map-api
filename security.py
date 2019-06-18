from functools import wraps
from flask import request, abort

APPKEY_HERE='eb8b1a9405e659b2ffc78f0a520b1a46'


def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if request.headers.get('X-Api-Key') and request.headers.get('X-Api-Key') == APPKEY_HERE:
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function

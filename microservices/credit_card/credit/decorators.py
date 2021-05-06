import jwt

from functools import wraps

from django.conf import settings

from rest_framework.response import Response

def token_required(view_func):
    def _decorated(request, *args, **kwargs):
        token = str(request.headers['Authorization']).replace('Bearer ', '')
        if not token:
            raise ValueError(f'Token is missing or wrong: {token}')
        try:
            data = jwt.decode(
                jwt=token,
                secret=settings.SECRET_KEY,
                algorithms=["HS256"],
                options={"verify_signature": False}
            )
        except Exception as e:
            raise ValueError('Error to auth token: {}'.format(str(e)))
        user_id = int(data['id'])
        return view_func(request, user_id, *args, **kwargs)
    return wraps(view_func)(_decorated)

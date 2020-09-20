import json
import jwt
import re

from django.http        import JsonResponse

from .models            import User

from pilly.settings     import (
    SECRET_KEY,
    ALGORITHM
)

class LoginConfirm:
    def __init__(self, func):
        self.func = func

    def __call__(self, request, *args, **kwargs):
        token = request.headers.get("Authorization", None)
        try:
            if token:
                payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
                user = User.objects.get(id = payload['user'])
                request.user = user
                return self.func(self, request, *args, **kwargs)
            return JsonResponse({'message': 'NEED_LOGIN'}, status=401)

        except jwt.ExpiredSignatureError:
            return JsonResponse({'message': 'EXPIRED_TOKEN'}, status=401)

        except jwt.DecodeError:
            return JsonResponse({'message': 'INVALID_USER'}, status=401)

        except User.DoesNotExist:
            return JsonResponse({'message': 'INVALID_USER'}, status=401)


def deco_vali_name():
    def validation_name(name):
        name_validator = re.compile('[가-힣]{2,5}')
        return bool(lambda name: name_validator.match(name))
    return validation_name

def deco_vali_email():
    def validation_email(email):
        if User.objects.filter(email = email).exists():
            return False
    
        email_validator = re.compile('^[a-zA-Z0-9+.-_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$')
        return bool(lambda email: email_validator.match(email))
    return validation_email

def deco_vali_contact():
    def validation_contact(contact):
        contact_validator = re.compile('[0-9]{10,11}')
        return bool(lambda contact: contact_validator.match(contact))
    return validation_contact

def deco_vali_password():
    def validation_password(password):
        password_validator = re.compile('[a-zA-Z0-9!?@*+.,^&%]{8,20}')
        return bool(lambda password: password_validator.match(password))
    return validation_password

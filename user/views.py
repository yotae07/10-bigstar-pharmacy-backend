import json
import bcrypt
import jwt
import re

from django.views     import View
from django.http      import JsonResponse

from .models          import User
from .utils           import LoginConfirm 
from pilly.settings   import (
    SECRET_KEY,
    ALGORITHM
)

def LogInCheck(user, pwd):
    if user and bcrypt.checkpw(pwd.encode('utf-8'), user.password.encode('utf-8')):
        token = jwt.encode({'user': n.id}, SECRET_KEY, ALGORITHM).decode('utf-8')
        return JsonResponse({'token': token}, status=200)

def validation_name(name):
    check = [bool(lambda name: re.search("[가-힣]+$", name))]

    for i in check:
        if i != True:
            return False
        else:
            return True

def validation_email(email):
    if User.objects.filter(email = email).exists():
        return False
    email_split = email.split('@')
    email_check = email_split[0]
    check = [bool(lambda email_check: re.search("[a-zA-Z0-9]+$", email_check))]
    
    for i in check:
        if i != True:
            return False
        else:
            return True

def validation_contact(contact):
    check = [bool(lambda contact: re.search("[0-9]", contact))]

    for i in check:
        if i != True:
            return True
        else:
            return False

def validation_password(password):
    check = [
        bool(lambda password: any(x.isdigit() for x in password)),
        bool(lambda password: any(x.islower() for x in password)),
        bool(lambda password: any(x.isupper() for x in password)),
        bool(lambda password: len(password) == len(password.replace(" ", ""))),
        bool(lambda password: len(password) >= 5)
        ]

    for i in check:
        if i != True:
            return False
        else:
            return True

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            validation_all = [
                validation_name(data['name']),
                validation_email(data['email']),
                validation_contact(data['contact']),
                validation_password(data['password'])
            ]
            for validation in validation_all:
                if validation != True:
                    return JsonResponse({'message': 'INVALID_INPUT'}, status=401)
                else:
                    User(
                        name     = data['name'],
                        email    = data['email'],
                        contact  = data['contact'],
                        password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                    ).save()
                    return JsonResponse({'message': 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=401)

class SignInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data.get("email")
            contact = data.get("contact")
            password = data.get("password")

            if email:
                user_qs = User.objects.get(email=email)
                return LogInCheck(user_qs, password)
            elif contact:
                user_qs = User.objects.get(contact=contact)
                return LogInCheck(user_qs, password)
            return JsonResponse({'message': 'NOT_EXISTS'}, status=401)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status= 401)
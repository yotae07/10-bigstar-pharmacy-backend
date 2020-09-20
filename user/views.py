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
        token = jwt.encode({'user': user.id}, SECRET_KEY, ALGORITHM).decode('utf-8')
        return JsonResponse({'token': token}, status=200)

def deco_vali_name():
    def validation_name(name):
        name_validator = re.compile('^[가-힣]{2,5}$')
        check = lambda name: bool(name_validator.match(name))
        return check(name)
    return validation_name

def deco_vali_email():
    def validation_email(email):
        if User.objects.filter(email = email).exists():
            return False
    
        email_validator = re.compile('^[a-zA-Z0-9+.-_]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$')
        check = lambda email: bool(email_validator.match(email))
        return check(email)
    return validation_email

def deco_vali_contact():
    def validation_contact(contact):
        contact_validator = re.compile('^[0-9]{10,11}$')
        check = lambda contact: bool(contact_validator.match(contact))
        return check(contact)
    return validation_contact

def deco_vali_password():
    def validation_password(password):
        password_validator = re.compile('^[a-zA-Z0-9!?@*+-_&%]{8,20}$')
        check = lambda password: bool(password_validator.match(password))
        return check(password)
    return validation_password

vali1 = deco_vali_name()
vali2 = deco_vali_email()
vali3 = deco_vali_contact()
vali4 = deco_vali_password()

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            vali = [vali1, vali2, vali3, vali4]
            for content, check in zip(vali, list(data.values())):
                if not content(check):
                    return JsonResponse({'message': 'INVALID_INPUT'}, status=401)
            #User(
            #    name = data['name'],
            #    email = data['email'],
            #    contact = data['contact'],
            #    password = data['password']
            #).save()
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

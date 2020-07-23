import json, bcrypt, jwt, re

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from .models          import User
from .utils           import LoginConfirm 
from pilly.settings   import SECRET_KEY, ALGORITHM

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            if bool(re.search("[가-힣]+$", data['name'])) != True:
                return JsonResponse({'message': 'ONLY_KOREAN'}, status=401)
            elif User.objects.filter(email = data['id']).exists():
                return JsonResponse({'message': 'EXIST_EMAIL'}, status=401)
            elif bool(re.search("(\d{11})", data['contact'])) != True:
                return JsonResponse({'message': 'INVALID_NUBER_INPUT'}, status=401)
            elif data['password'] != data['check_password']:
                return JsonResponse({'message': 'INVALID_PASSWORD'}, status=401)
            elif data['id']:
                email_check = data['id'].split('@')
                email_bool  = bool(re.search("[a-zA-Z0-9]+$", email_check[0]))
                if email_bool != True:
                    return JsonResponse({'message': 'INVLID_EMAIL'}, status=401)
                else:
                    User(
                        name          = data['name'],
                        email         = data['id'],
                        mobile_number = data['contact'],
                        password      = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                    ).save()
                return JsonResponse({'message': 'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=401)

class SignInView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            if User.objects.filter(email = data['id']).exists():
                user = User.objects.filter(email = data['id'])
                if bcrypt.checkpw(data['password'].encode('utf-8'), user[0].password.encode('utf-8')):
                    access_user = User.objects.get(email = data['id'])
                    token       = jwt.encode({'user': access_user.id}, SECRET_KEY, ALGORITHM).decode('utf-8')
                    return JsonResponse({'token': token}, status=200)
                return JsonResponse({'message': 'INVALID_PASSWORD'}, status=401)
            elif User.objects.filter(mobile_number = data['contact']).exists():
                user = User.objects.filter(mobile_number = data['contact'])
                print('asfd')
                if bcrypt.checkpw(data['password'].encode('utf-8'), user[0].password.encode('utf-8')):
                    print('ccc')
                    access_user = User.objects.get(mobile_number = data['contact'])
                    token       = jwt.encode({'user': access_user.id}, SECRET_KEY, ALGORITHM).decode('utf-8')
                    return JsonResponse({'token': token}, status=200)
                return JsonResponse({'message': 'INVLID_PASSWORD'}, status=401)
            return JsonResponse({'message': 'INVLID_INPUT'}, status=401)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=401)



import json
import bcrypt
import jwt

from instagram.settings import SECRET_KEY
from .models import Account

from django.views import View
from django.http  import HttpResponse, JsonResponse

class AccountView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if Account.objects.filter(email=data['email']).exists():
                return JsonResponse({'message':'USER_ALREADY_EXISTS'}, status = 400)

            password = data['password'].encode('utf-8')
            encrypted_pw = bcrypt.hashpw(password, bcrypt.gensalt())
            encrypted_pw = encrypted_pw.decode('utf-8')
        
            Account(
                name     = data['name'],
                email    = data['email'],
                password = encrypted_pw
            ).save()

            return HttpResponse(status = 200)

        except KeyError:
            return JsonResponse({"message" : "INVALID_KEYS"}, status = 400)

class LogInView(View):
    def post(self, request):
        data = json.loads(request.body) 

        try:
            if Account.objects.filter(email = data['email']).exists():
                user = Account.objects.get(email = data['email'])

                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):

                    token = jwt.encode({'email' : data['email']}, SECRET_KEY, algorithm = 'HS256')
                    token = token.decode('utf-8')

                    return JsonResponse({"token" : token}, status = 200)

                else:
                    return HttpResponse(status=401)

            return JsonResponse({'message':'USER_NOT_FOUND'}, status = 400)

        except KeyError:
            return JsonResponse({'message':'INVALID_KEYS'}, status = 400)



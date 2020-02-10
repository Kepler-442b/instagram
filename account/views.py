import json

from .models import Account

from django.views import View
from django.http  import HttpResponse, JsonResponse

class AccountView(View):
    def post(self, request):
        data = json.loads(request.body)

        if Account.objects.filter(email=data['email']).exists():
            return JsonResponse({'message':'USER_ALREADY_EXISTS'}, status = 400)
        
        Account(
            name     = data['name'],
            email    = data['email'],
            password = data['password']
        ).save()

        return HttpResponse(status = 200)

    def get(self, request):
        account_data = Account.objects.values()
        return JsonResponse({'account':list(account_data)}, status = 200)

class LogInView(View):
    def post(self, request):
        data = json.loads(request.body) 
        try:
            if Account.objects.filter(email=data['email']).exists():
                user = Account.objects.get(email=data['email'])

                if data['password'] == user.password:
                    return JsonResponse({'message':'SUCCESS'}, status = 200)
                return HttpResponse(status=401)

            return JsonResponse({'message':'USER_DOES_NOT_EXIST'}, status = 400)

        except KeyError:
            return JsonResponse({'message':'INVALID_KEY'}, status = 400)

import json

from .models import Account

from django.views import View
from django.http import HttpResponse, JsonResponse

class AccountView(View):
    def post(self, request):
        data = json.loads(request.body)
        Account(
            name     = data['name'],
            email    = data['email'],
            password = data['password']
        ).save()

        return HttpResponse(status = 200)

    def get(self, request):
        account_data = Account.objects.values()
        return JsonResponse({'account':list(account_data)}, status = 200)

      #  account_data =  Account.objects.all()
      #  accounts = []
      #  for account in account_data:
      #      accounts.append({
      #          'name': account.name,
      #          'email': account.email,
      #          'password': account.password
      #          })
      #  print(accounts)

class LogInView(View):
    def post(self, request):
        data = json.loads(request.body)
        user_email = data['email']
        user_pw    = data['password']
        existing_user_email = Account.objects.get(email=user_email)
        existing_user_pw = Account.objects.get(password=user_pw)
        try:
            user_email = existing_user_email
            try:
                user_pw == existing_user_pw
            except:
                return JsonResponse({'message':'password does not match'}, status=401)
        except Account.DoesNotExist:
            return JsonResponse({'message':'user does not exist'}, status = 401)
        return JsonResponse({'message':'success'}, status = 200)


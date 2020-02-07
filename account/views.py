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
        # 유저가 입력한 값 json 포맷으로 바꿔주기
        data = json.loads(request.body)
        # 유저가 입력한 email과 pw 변수에 등록
        user_email = data['email']
        user_pw = data['password']
        # Account에 들어있는 요소 불러오기
        existing_users = Account.objects.values()
        # 유저입력값과 Account의 요소비교
        for user in existing_users:
            for key in user:
                if  user['email'] == user_email and user['password'] == user_pw:
                    return JsonResponse({'message':'log in success'}, status = 200)
                else:
                    return JsonResponse({'message':'try again'}, status = 404)


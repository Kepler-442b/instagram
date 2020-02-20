import jwt
import json
import requests

from django.http                        import JsonResponse
from django.core.exceptions             import ObjectDoesNotExist

from instagram.settings                 import SECRET_KEY 
from .models                            import Account

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None) #http headers에서 토큰을 받아온다
            payload      = jwt.decode(access_token, SECRET_KEY, algorithm = 'HS256')  #받아온토큰을 decode
            user         = Account.objects.get(email=payload["email"]) #decode해서 나온 정보와 매칭하는정보
            request.user = user #func에서 사용

        except jwt.DecodeError:
            return JsonResponse({'message' : 'INVALID_TOKEN'}, status = 401)

        except User.DoesNotExist:
            return JsonResponse({'message':'INVALID_USER'}, status = 400)

        except TypeError:
            return JsonResponse({'message':'INVALID_VALUE'}, status = 400)

        except KeyError:
            return JsonResponse({'message': 'INVALID'}, status = 400)

        return func(self, request, *args, **kwargs)

    return wrapper


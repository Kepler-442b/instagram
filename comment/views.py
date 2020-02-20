import json

from .models import Comment
from account.utils import login_decorator

from django.views import View
from django.http import HttpResponse, JsonResponse

class CommentView(View):
    @login_decorator
    def post(self, request):
        data = json.loads(request.body)
        Comment(
                email = data['email'],
                text = data['text']
                ).save()
        return HttpResponse(status = 200)
    
    @login_decorator
    def get(self, request):
        return JsonReponse({'comment' : list(Comment.objects.values())}, status = 200)




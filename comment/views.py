import json

from .models import Comment

from django.views import View
from django.http import HttpResponse, JsonResponse

class CommentView(View):
    def post(self, request):
        data = json.loads(request.body)
        Comment(
                name = data['name'],
                text = data['text']
                ).save()
        return HttpResponse(status = 200)
    
    def get(self, request):
        comment_data = Account.objects.values()
        return JsonReponse({'comment':list(comment_data)}, status = 200)




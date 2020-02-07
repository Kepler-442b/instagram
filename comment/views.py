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



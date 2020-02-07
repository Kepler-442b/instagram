from django.urls import path
from .views import AccountView, LogInView

urlpatterns = [
    path('/sign-up', AccountView.as_view()),
    path('', AccountView.as_view()),
    path('/log-in', LogInView.as_view()),
#    path('/comments', CommentView.as_view()),
    ]

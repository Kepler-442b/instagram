from django.db import models

class Comment(models.Model):
    email      = models.CharField(max_length = 500, default='user_email')
    text       = models.CharField(max_length = 3000)
    create_at  = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'comments'

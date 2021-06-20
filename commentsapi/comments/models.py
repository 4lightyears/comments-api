from django.db import models

# Create your models here.

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True, blank=False)
    description = models.CharField(max_length=200, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.description)


class Reply(models.Model):
    reply_id = models.AutoField(primary_key=True, blank=False)
    description = models.CharField(max_length=200, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.description)

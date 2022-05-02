from django.db import models

# Create your models here.


class Comment(models.Model):
    """Model for Comment"""

    comment_id = models.AutoField(primary_key=True, blank=False)
    description = models.CharField(max_length=200, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    class Meta:
        """Additional settings for the model"""
        db_table = 'comment'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return f'{self.description}'


class Reply(models.Model):
    """Model for Reply"""

    reply_id = models.AutoField(primary_key=True, blank=False)
    description = models.CharField(max_length=200, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)

    objects = models.Manager()

    class Meta:
        """Additional settings for the model"""
        db_table = 'reply'
        verbose_name = 'reply'
        verbose_name_plural = 'replies'

    def __str__(self):
        return f'{self.description}'

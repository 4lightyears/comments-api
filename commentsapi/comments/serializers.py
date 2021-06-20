from rest_framework import serializers

from .models import Comment, Reply


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'comment_id', 'description', 'created_at', 'updated_at'
        )

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = (
            'reply_id', 'description', 'created_at', 'updated_at', 'comment_id_id'
        )

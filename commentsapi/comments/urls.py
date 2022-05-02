from django.urls import path

from .views import AllComments, CommentDetail, ReplyDetail, CreateReply


urlpatterns = [
    path('comments', AllComments.as_view()),
    path('comment/<int:comment_id>', CommentDetail.as_view()),
    path('comment/reply', CreateReply.as_view()),
    path('comment/reply/<int:reply_id>', ReplyDetail.as_view()),
]

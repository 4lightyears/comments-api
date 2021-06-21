from django.urls import path

from . import views


urlpatterns = [
    path('comments', views.comments_view),
    path('comment/<int:comment_id>', views.comment_view),
    path('comment/reply', views.create_reply_view),
    path('comment/reply/<int:reply_id>', views.modify_reply_view),
]

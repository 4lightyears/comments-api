from django.urls import path

from . import views


urlpatterns = [
    path('comments', views.comments_view),
    path('comment/<int:comment_id>', views.comment_view),
]

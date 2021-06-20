from django.urls import path

from . import views


urlpatterns = [
    path('comments', views.AllCommentsView.as_view()),
]

from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.views import View

from rest_framework.parsers import JSONParser
from rest_framework import viewsets, status
from rest_framework.decorators import api_view

from .models import Comment, Reply
from .serializers import CommentSerializer, ReplySerializer


# @api_view(('GET', 'POST'))
# def comments_list(request):
#     if request.method == 'GET':
#         all_comments = Comment.objects.all()
#         all_replies = Reply.objects.all()
#
#         comment_serializer = CommentSerializer(all_comments, many=True)
#         reply_serializer = ReplySerializer(all_replies, many=True)
#
#         comments_data, replies_data = comment_serializer.data, reply_serializer.data
#
#
#         return JsonResponse(comment_serializer.data, safe=False)

class AllCommentsView(View):
    def get(self, request):
        all_comments = Comment.objects.all()
        all_replies = Reply.objects.all()

        comment_serializer = CommentSerializer(all_comments, many=True)
        reply_serializer = ReplySerializer(all_replies, many=True)

        comments_data, replies_data = comment_serializer.data, reply_serializer.data

        return JsonResponse(comments_data, safe=False)


# class CommentView(View):
#     def get(self, request, comment_id):
#         pass
#
#     def post(self, request):
#         pass
#
#     def put(self, request):
#         pass
#
#     def delete(self, request):
#         pass

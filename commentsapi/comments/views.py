from sqlite3 import IntegrityError

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework import status

from .models import Comment, Reply
from .serializers import CommentSerializer, ReplySerializer


@csrf_exempt
def comments_view(request):
    if request.method == 'GET':
        all_comments = Comment.objects.all()
        all_replies = Reply.objects.all()

        comment_serializer = CommentSerializer(all_comments, many=True)
        reply_serializer = ReplySerializer(all_replies, many=True)

        comments_data, replies_data = comment_serializer.data, reply_serializer.data

        final_list = []
        for i in comments_data:
            data = {}
            replies_list = []
            data['comment_id'] = i['comment_id']
            data['description'] = i['description']
            for j in replies_data:
                if i['comment_id'] == j['comment_id_id']:
                    replies_list.append({
                        'reply_id': j['reply_id'],
                        'description': j['description']
                    })
            data['replies'] = replies_list
            final_list.append(data)

        return JsonResponse({"comments": final_list}, safe=False)

    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
        except:
            print('error')
            return JsonResponse({'message': 'improper json formatting in body.'}, status=status.HTTP_400_BAD_REQUEST)
        print(data)
        comment_serializer = CommentSerializer(data=data)
        if comment_serializer.is_valid():
            try:
                comment_serializer.save()
            except IntegrityError as e:
                return JsonResponse({'message': 'error saving data to the database'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return JsonResponse(comment_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def comment_view(request, comment_id):

    try:
        data = Comment.objects.get(comment_id=comment_id)
    except:
        return JsonResponse({'message': 'Comment does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            comment = Comment.objects.filter(comment_id=comment_id)
        except ValueError as ve:
            return JsonResponse({'message': 'Improper value for comment_id'}, status=status.HTTP_400_BAD_REQUEST)
        reply = Reply.objects.all().filter(comment_id_id=comment_id).all()

        serialized_comment = CommentSerializer(comment, many=True)
        serialized_reply = ReplySerializer(reply, many=True)

        replies_list = []
        for i in serialized_reply.data:
            data = {
                'reply_id': i['reply_id'],
                'description': i['description']
            }

            replies_list.append(data)
        try:
            serialized_comment.data[0]['replies'] = replies_list
        except IndexError as ie:
            return JsonResponse({'message': 'not found.'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'comment': serialized_comment.data}, safe=False)

    if request.method == 'PUT':
        try:
            data = JSONParser().parse(request)
        except:
            return JsonResponse({'message': 'improper foramtting for json body in request.'}, status=status.HTTP_400_BAD_REQUEST)
        comment_serializer = CommentSerializer(data=data)
        if comment_serializer.is_valid():
            Comment.objects.filter(comment_id=comment_id).update(description=data['description'])
            return JsonResponse(comment_serializer.data, status=status.HTTP_202_ACCEPTED)
        return JsonResponse(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        Comment.objects.filter(comment_id=comment_id).delete()
        return JsonResponse({'message': 'Deleted'}, status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def create_reply_view(request):


    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        reply_serializer = ReplySerializer(data=data)
        if reply_serializer.is_valid():
            try:
                reply_serializer.create(data)
            except:
                return JsonResponse({'message': ''}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return JsonResponse(reply_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(reply_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def modify_reply_view(request, reply_id):

    try:
        data = Reply.objects.get(reply_id=reply_id)
    except:
        return JsonResponse({'message': 'Reply does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        try:
            data = JSONParser().parse(request)
        except:
            return JsonResponse({'message': 'improper foramtting for json body in request.'})
        reply_serializer = ReplySerializer(data=data)
        if reply_serializer.is_valid():
            Reply.objects.filter(reply_id=reply_id).update(description=data['description'])
            return JsonResponse(reply_serializer.data, status=status.HTTP_202_ACCEPTED)
        return JsonResponse(reply_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        Reply.objects.filter(reply_id=reply_id).delete()
        return JsonResponse({'message': 'Deleted'}, status=status.HTTP_204_NO_CONTENT)

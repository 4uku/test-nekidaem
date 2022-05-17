from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, BlogFollow, Blog

User = get_user_model()


class AddPostApi(APIView):
    permission_classes = [IsAuthenticated]

    class InputSerializer(serializers.Serializer):
        title = serializers.CharField(max_length=20, required=True)
        text = serializers.CharField(max_length=140, required=True)

        def validate(self, data):
            request = self.context.get('request', None)
            if request:
                user = request.user
            title = data.get('title')
            if Post.objects.filter(author=user, title=title).exists():
                raise serializers.ValidationError(
                    detail={'error': 'Пост с таким заголовком уже имеется'},
                    code=status.HTTP_400_BAD_REQUEST
                )
            return data

    def post(self, request):
        serializer = self.InputSerializer(
            data=request.data, context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        Post.objects.create(author=request.user, **serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)


class FollowBlogApi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, blog_id):
        blog = get_object_or_404(Blog, id=blog_id)
        if blog.author == request.user:
            return Response(
                'Подписка на самого себя запрещена',
                status=status.HTTP_400_BAD_REQUEST
            )
        obj, statement = BlogFollow.objects.get_or_create(
            blog=blog, follower=request.user)
        if statement:
            return Response(
                'Подписка осуществлена', status=status.HTTP_201_CREATED
            )
        return Response(
            'Вы уже подписаны на данного автора',
            status=status.HTTP_400_BAD_REQUEST
        )

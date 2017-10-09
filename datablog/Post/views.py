from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Post, Tag
from .serializers import PostSerializer, TagSerializer


@api_view(['GET'])
def posts_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def tags_list(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def post_details(request, slug):
    try:
        post = Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)


@api_view(['GET'])
def tag_posts(request, slug):
    if request.method == 'GET':
        posts = Post.objects.filter(tags__slug=slug)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

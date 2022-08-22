from django.shortcuts import render
from .models import Post
from .serializers import PostSerializers
from django.http import JsonResponse
from rest_framework.decorators import api_view
# Create your views here.

@api_view( ['GET'] )
def posts( request ):
    posts = Post.objects.all()
    serialized_posts = PostSerializers( posts, many=True)
    return JsonResponse( serialized_posts.data, safe=False)

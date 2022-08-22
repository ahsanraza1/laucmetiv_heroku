from django.shortcuts import render
from .models import Post
from .serializers import PostSerializers
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view( ['GET'] )
def posts( request ):
    posts = Post.objects.all()
    serialized_posts = PostSerializers( posts, many=True)
    return JsonResponse( serialized_posts.data, safe=False)


# @api_view( ['GET'] )
def main( request ):
    return HttpResponse( '<h1>This url is working fine</h1>')

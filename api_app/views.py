from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Blog 
from .serializer import Blogserializer

# Create your views here.
@api_view(['GET'])
def all_blogs(request):
    blogs = Blog.objects.all()
    serializer = Blogserializer(blogs, many = True)
    return Response(serializer.data)


@api_view(['POST'])
def createblog(request):
    serializer = Blogserializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def get_blog(request, pk):
    try:
        blog = Blog.objects.get(pk = pk)
    except Blog.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = Blogserializer(blog)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = Blogserializer(blog, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        blog.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)



from django.shortcuts import render
from rest_framework import generics, permissions
from articles.models import Article
from .serializers import ArticleSerializer
from .permissions import IsAuthorOrReadOnly
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def postCreate(request):
    serializer = ArticleSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

class ArticleAPIView(generics.ListAPIView):
    permission_classes = (IsAuthorOrReadOnly,) 
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) 
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
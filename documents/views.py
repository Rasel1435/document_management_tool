from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Document, Access
from .serializers import DocumentSerializer, AccessSerializer
# from flask import request
# Create your views here.

class DocumentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class DocumentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class AccessListCreateAPIView(generics.ListCreateAPIView):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer

class AccessRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer
    
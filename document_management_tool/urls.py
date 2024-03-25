"""
URL configuration for document_management_tool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from documents.views import DocumentListCreateAPIView, DocumentRetrieveUpdateDestroyAPIView
from documents.views import AccessListCreateAPIView, AccessRetrieveUpdateDestroyAPIView
from rest_framework_swagger.views import get_swagger_view
from document_management_tool.views import home
# from . import views

schema_view = get_swagger_view(title='Document Management API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('documents/', DocumentListCreateAPIView.as_view(), name='document-list-create'),
    path('documents/<int:pk>/', DocumentRetrieveUpdateDestroyAPIView.as_view(), name='document-retrieve-update-destroy'),
    path('access/', AccessListCreateAPIView.as_view(), name='access-list-create'),
    path('access/<int:pk>/', AccessRetrieveUpdateDestroyAPIView.as_view(), name='access-retrieve-update-destroy'),
    path('swagger-docs/', schema_view),
]

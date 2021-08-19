from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def home(request):
    return Response({'status':200,'messages':"hello django rest-framework"})



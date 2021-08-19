
from django.urls import path
from smallapp import views

urlpatterns = [
  path('',views.home),
]

from django.urls import path
from  . import views

urlpatterns = [
    path('', views.CustomAuthToken.as_view(), name='signup'), 
]

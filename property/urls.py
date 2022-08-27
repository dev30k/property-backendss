from django.urls import path
from  . import views

urlpatterns = [
    path('api/v1/appProperty/', views.PropertyView.as_view(), name='property add'), 
]

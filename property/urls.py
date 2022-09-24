from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/addProperty/', views.PropertyView.as_view(), name='property'),
    path('api/v1/addProperty/residential/', views.ResidentialPropertyView.as_view(), name='residental')
]

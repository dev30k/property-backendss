from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/appProperty/', views.PropertyView.as_view(), name='property'),
    path('api/v1/appProperty/residental/', views.ResidentailPropertyView.as_view(), name='residental')
]

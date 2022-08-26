from django.urls import path
from  . import views

urlpatterns = [
    path('api/v1/signup/', views.SignInUserView.as_view(), name='signup'), 
    path('api/v1/login/', views.LoginUserView.as_view(), name='user_login'),
    path('api/v1/logout/', views.LogoutUserView.as_view(), name='user_logout'),
]

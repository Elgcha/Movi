from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('profile/edit/', views.profile_edit),
    path('active/', views.user_active),
    #login
    path('api-token-auth/', obtain_jwt_token),
    path('api/token/verify/', verify_jwt_token),
    # 유저 권한 확인
    path('check/', views.user_check),
] 
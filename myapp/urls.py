from .import views
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
      
    path('login_token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),name='token_refresh'),
    path('register/', views.RegisterUser.as_view()),
    path('change_password/<int:pk>/', views.ChangePasswordView.as_view(), name='auth_change_password'),
]
     


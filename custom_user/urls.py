from django.urls import path
from .apps import CustomUserConfig
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CustomUserListView, CustomUserCreateView


app_name = CustomUserConfig.name


urlpatterns = [
    path('', CustomUserListView.as_view(), name='custom_user_list'),
    path('create/', CustomUserCreateView.as_view(), name='custom_user_create'),

    # authorization urls
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

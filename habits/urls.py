from django.urls import path
from .apps import HabitsConfig
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import HabitsListView, HabitsCreateView, PublicHabitsListView, HabitsUpdateView, HabitsDeleteView


app_name = HabitsConfig.name


urlpatterns = [
    path('', HabitsListView.as_view(), name='habits_list'),
    path('public-habits/', PublicHabitsListView.as_view(), name='public_habits_list'),
    path('create/', HabitsCreateView.as_view(), name='habits_create'),
    path('update/<int:pk>/', HabitsUpdateView.as_view(), name='habits_update'),
    path('delete/<int:pk>/', HabitsDeleteView.as_view(), name='habits_delete'),

    # authorization urls
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

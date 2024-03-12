from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.urls import path
from .views import *


urlpatterns = [

    path('categories/', CategoryAPIView.as_view()),
    path('categories/create/', CategoryAPICreate.as_view()),
    path('categories/updateOrdeleted/<int:pk>/',CategoryUpdateOrDeletedAPIView.as_view()),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view()),
    path('articles/',BlogPostAPIView.as_view()),
    path('articles/create/',BlogPostCreateAPIView.as_view()),
    path('article/updateOrdeleted/<int:pk>/', BlogPostUpdateOrDeleted.as_view()),
    path('article/<int:pk>/', BlogPostDetailAPIView.as_view()),
    path('articles/published/',BlogPostPublishedTrue.as_view()),
    path('users/login/', TokenObtainPairView.as_view()),
    path('users/login/refresh/', TokenRefreshView.as_view()),
    path('users/login/verify/', TokenVerifyView.as_view()),
    path('users/register/', RegisterView.as_view()),
    path('users/me/', RetrieveUserView.as_view()),
    path('users/updateOrdeleted/<int:pk>/', UserAcccountAPIViewUpdateOrDelete.as_view()),
    path('users/', UserAccountAPIView.as_view()),
]
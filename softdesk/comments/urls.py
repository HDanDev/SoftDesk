from django.urls import path
from . import views

urlpatterns = [
    path('api/comments/', views.CommentList.as_view(), name='comment-list'),
    path('api/comments/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'),
]

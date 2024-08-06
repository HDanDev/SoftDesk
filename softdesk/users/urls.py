from django.urls import path
from . import views

urlpatterns = [
    path('api/users/', views.UserList.as_view(), name='user-list'),
    path('api/contributors/', views.ContributorList.as_view(), name='contributor-list'),
]

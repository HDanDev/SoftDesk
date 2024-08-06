from django.urls import path
from . import views

urlpatterns = [
    path('api/issues/', views.IssueList.as_view(), name='issue-list'),
    path('api/issues/<int:pk>/', views.IssueDetail.as_view(), name='issue-detail'),
]

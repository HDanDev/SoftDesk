from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ContributorViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'contributors', ContributorViewSet, basename='contributor')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]

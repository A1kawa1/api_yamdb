from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import *


router = DefaultRouter()
router.register('titles', TitlesViewSet, basename='titles')
router.register('genres', GenreViewSet, basename='genres')
router.register('categories', TitlesViewSet, basename='categories')

urlpatterns = [
    path('v1/', include(router.urls))
]

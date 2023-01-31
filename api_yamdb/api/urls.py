from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import *


router = DefaultRouter()
router.register('titles', TitlesViewSet, basename='titles')
router.register('genres', GenreViewSet, basename='genres')
router.register('categories', TitlesViewSet, basename='categories')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
urlpatterns = [
    path('v1/', include(router.urls))
]

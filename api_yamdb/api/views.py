from rest_framework import viewsets
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    DestroyModelMixin
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from api.serializers import *
from model.models import *


class GetPostDestroy(
    ListModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializerRead

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PATCH'):
            return TitleSerializerCreate
        return TitleSerializerRead


class GenreViewSet(GetPostDestroy):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,) #нужен пермишен (админ или чтение)
    pagination_class = PageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'slug')
    lookup_field = 'slug'


class CategoryViewSet(GetPostDestroy):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,) #нужен пермишен (админ или чтение)
    pagination_class = PageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'slug')
    lookup_field = 'slug'


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    #permission_classes = нужен пермишен

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return title.review.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    #permission_classes = нужен пермишен

    def get_queryset(self):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        return review.comments.all()

    def perform_create(self, serializer):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        serializer.save(author=self.request.user, review=review)

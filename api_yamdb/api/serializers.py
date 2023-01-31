from rest_framework import serializers
from django.shortcuts import get_object_or_404
from datetime import datetime
from model.models import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            'name',
            'slug'
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
            'slug'
        )


class TitleSerializerRead(serializers.ModelSerializer):
    category = CategorySerializer(
        many=False,
        required=True
    )
    genre = GenreSerializer(
        many=True,
        required=False
    )
    rating = serializers.IntegerField()

    class Meta:
        model = Title
        fields = (
            'id'
            'name',
            'year',
            'description',
            'genre',
            'category',
            'rating'
        )
        read_only_fields = (
            'id',
            'name',
            'year',
            'rating',
            'description',
            'genre',
            'category'
        )


class TitleSerializerCreate(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug',
        many=False
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True,
        required=False,
    )

    class Meta:
        model = Title
        fields = (
            'id',
            'name',
            'year',
            'description',
            'genre',
            'category'
        )

    def validate_year(self, data):
        if not (0 <= data <= datetime.now().year):
            raise serializers.ValidationError(
                'недопустимая дата'
            )
        return data


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        default=serializers.CurrentUserDefault(),
        read_only=True
    )

    class Meta:
        model = Review
        fields = (
            'id',
            'text',
            'title',
            'author',
            'score',
            'pub_date'
        )
        read_only_fields = ('title',)

    def validate(self, data):
        request = self.context.get('request')
        author = request.user
        if request.method == 'POST':
            title_id = self.context.get('view').kwargs.get('title_id')
            title = get_object_or_404(Title, pk=title_id)
            if Review.objects.filter(
                    author=author,
                    title=title
            ).exists():
                raise serializers.ValidationError(
                    'нельзя оставить отзыв дважды'
                )
        return data

    def validate_score(self, value):
        if 0 >= value >= 10:
            raise serializers.ValidationError(
                'недопустимая оценка'
            )
        return value


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        default=serializers.CurrentUserDefault(),
        read_only=True
    )
    # review = serializers.SlugRelatedField(
    #     slug_field='text', read_only=True
    # )

    class Meta:
        model = Comment
        fields = (
            'id',
            'text',
            'author',
            'pub_date',
            # 'review'
        )
        # read_only = ('review',)

from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
)
from model.validators import year_validate
from user.models import User


class Title(models.Model):
    name = models.CharField(
        verbose_name='name',
        max_length=200
    )
    year = models.IntegerField(
        verbose_name='release year',
        validators=(year_validate,)
    )
    description = models.TextField(
        verbose_name='description',
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(
        'Genre',
        through='GenreTitle',
        blank=True
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        default_related_name = 'title'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(
        verbose_name='name',
        max_length=256
    )
    slug = models.SlugField(
        verbose_name='slug',
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        verbose_name='name',
        max_length=256
    )
    slug = models.SlugField(
        verbose_name='slug',
        max_length=50,
        unique=True
    )


    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'{self.genre} {self.title}'


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField(
        verbose_name='pub date',
        auto_now_add=True,
        db_index=True
    )
    text = models.TextField()
    score = models.IntegerField(
        verbose_name='score',
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ],
    )

    class Meta:
        default_related_name = 'reviews'
        ordering = ['-pub_date']


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField(
        'Дата комментария',
        auto_now_add=True,
        db_index=True
    )
    text = models.TextField()

    class Meta:
        default_related_name = 'comments'
        ordering = ['-pub_date']

    def __str__(self):
        return self.author

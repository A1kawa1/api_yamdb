from django.db import models
from django.contrib.auth.models import AbstractUser


class Title(models.Model):
    name = models.CharField(
        verbose_name='name',
        max_length=200
    )
    
    year = models.IntegerField(
        verbose_name='release year',
    )
    description = models.TextField(
        verbose_name='description',
        blank=True,
        null=True
    )
    genre = models.ManyToManyField(
        'Genre',
        blank=True
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    rating = models.IntegerField(
        null=True,
        default=None
    )

    class Meta:
        default_related_name = 'title'
        ordering = ('name',)

    def __str__(self):
        return self.name


class GenreAndCategory(models.Model):
    name = models.CharField(
        verbose_name='name',
        max_length=256
    )
    slug = models.SlugField(
        verbose_name='slug',
        max_length=50,
        unique=True
    )

    class Meta:
        abstract = True
        ordering = ('name',)

    def __str__(self):
        return self.name


class Genre(GenreAndCategory):
    pass


class Category(GenreAndCategory):
    pass


class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),
    )

    email = models.EmailField(
        verbose_name='email',
        unique=True,
    )
    role = models.CharField(
        max_length=255,
        choices=ROLE_CHOICES,
        default='user',
        verbose_name='role'
    )
    bio = models.TextField(
        blank=True,
        verbose_name='bio'
    )

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == 'admin'

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    @property
    def is_user(self):
        return self.role == 'user'
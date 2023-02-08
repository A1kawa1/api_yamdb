from django.urls import path
from api.v1.views import register, get_jwt_token


urlpatterns = [
    path('signup/', register, name='register'),
    path('token/', get_jwt_token, name='token')
]

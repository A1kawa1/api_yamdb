from django.urls import include, path


urlpatterns = [
    path('v1/', include('api.v1.urls')),
    path('v1/auth/', include('api.auth.urls')),
]

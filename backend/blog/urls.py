from rest_framework.routers import DefaultRouter
from django.urls import include, path
from . import views

router = DefaultRouter()
router.register('posts', views.PostViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]
from rest_framework import routers
from image_generation.views import ImageGenerationView
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter()
router.register(r"image_generation", ImageGenerationView, basename="image_generation")

urlpatterns = [
    path("", include(router.urls)),
]

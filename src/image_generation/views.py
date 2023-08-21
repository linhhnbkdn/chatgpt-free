from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from openai import Image as OpenAIImage
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import UserRateThrottle
from rest_framework.throttling import AnonRateThrottle

from django.conf import settings

class ImageGenerationView(GenericViewSet):
    permission_classes = (AllowAny,)
    throttle_classes = (AnonRateThrottle,)

    @action(methods=['post'], detail=False)
    def generate(self, request):
        print(request.data)
        # OpenAIImage.create(
        #     api_key=settings.CHATGPT_API_KEY,
        #     prompt="a white siamese cat",
        #     n=1,
        #     size="1024x1024"
        # )
        return Response(status=status.HTTP_200_OK)

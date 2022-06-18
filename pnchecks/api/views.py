
from pnchecks.utils import pneumonia_check
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework_api_key.permissions import HasAPIKey
from rest_framework.permissions import IsAuthenticated

from .serializer import UploadSerializer


# ViewSets define the view behavior.
class ImageViewSet(ViewSet):
    """
    http POST http://localhost:8000/api/v1/image/accept/ X-API-Key:0K5wF1Tr.oYPI5A0BeXeFVDvmpbUCvP3wqzeV2O2n
    """
    serializer_class = UploadSerializer
    permission_classes = [HasAPIKey | IsAuthenticated]
    http_method_names = ['get', 'post', 'head']
    def list(self, request):
        return Response("PnCheck: Have Fun!! ")

    def post(self, request):
        try:
            image = request.FILES.get('image_uploaded')
        except KeyError:
            raise ParseError('Request has no resource image attached')
        result = pneumonia_check(image)
        return Response(result)


from pnchecks.utils import pneumonia_check

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from .serializer import UploadSerializer


# ViewSets define the view behavior.
class ImageViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("PnCheck: Have Fun!! ")

    def post(self, request):
        try:
            image = request.FILES.get('image_uploaded')
        except KeyError:
            raise ParseError('Request has no resource image attached')
        result = pneumonia_check(image)
        return Response(result)

from rest_framework.serializers import Serializer, ImageField


# Serializers define the API representation.
class UploadSerializer(Serializer):
    image_uploaded = ImageField()
    class Meta:
        fields = ['image_uploaded']
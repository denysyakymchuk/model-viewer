from rest_framework import viewsets

from .serializer import ThreeDModelSerializer
from .models import ThreeDModel


class ThreeDModelViewSet(viewsets.ModelViewSet):
    serializer_class = ThreeDModelSerializer
    queryset = ThreeDModel.objects.all()

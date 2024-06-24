from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as drf_filters

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action

from .serializer import ThreeDModelSerializer
from .models import ThreeDModel
from .filters import ThreeDModelFilter


class ThreeDModelViewSet(viewsets.ModelViewSet):
    serializer_class = ThreeDModelSerializer
    queryset = ThreeDModel.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    filterset_class = ThreeDModelFilter
    filter_backends = [DjangoFilterBackend, drf_filters.SearchFilter, drf_filters.OrderingFilter]
    ordering_fields = ['owner', 'id', 'time_create', 'time_update']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(detail=False, methods=['get'], url_path='users-models', permission_classes=[IsAuthenticated])
    def get_users_models(self, request):
        models = ThreeDModel.objects.filter(owner=self.request.user)
        serializer = self.get_serializer(models, many=True)
        return Response(serializer.data)
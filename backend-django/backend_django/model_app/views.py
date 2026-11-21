from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as drf_filters

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action

from .serializer import ThreeDModelSerializer
from .models import ThreeDModel
from .filters import ThreeDModelFilter
from .pagination import ModelMainPagePagination
from .utils import extract_usernames


class ThreeDModelViewSet(viewsets.ModelViewSet):
    serializer_class = ThreeDModelSerializer
    queryset = ThreeDModel.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = (IsAuthenticatedOrReadOnly,)

    filterset_class = ThreeDModelFilter
    filter_backends = [DjangoFilterBackend, drf_filters.SearchFilter, drf_filters.OrderingFilter]
    ordering_fields = ['owner', 'id', 'time_create', 'time_update']

    def partial_update(self, request, *args, **kwargs):
        if not ThreeDModel.objects.filter(id=kwargs['pk']).exists():
            return Response({'error': 'ThreeD Model does not exist'}, status=status.HTTP_404_NOT_FOUND)

        model_owner_object = ThreeDModel.objects.filter(id=kwargs.get('pk')).first()

        if model_owner_object.owner_id != request.user.id:
            return Response({'error': 'Unauthorized request'}, status=status.HTTP_403_FORBIDDEN)

        return super().partial_update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if not ThreeDModel.objects.filter(id=kwargs['pk']).exists():
            return Response({'error': 'ThreeD Model does not exist'}, status=status.HTTP_404_NOT_FOUND)

        model_owner_object = ThreeDModel.objects.filter(id=kwargs.get('pk')).first()

        if model_owner_object.owner_id != request.user.id:
            return Response({'error': 'Unauthorized request'}, status=status.HTTP_403_FORBIDDEN)

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not ThreeDModel.objects.filter(id=kwargs['pk']).exists():
            return Response({'error': 'ThreeD Model does not exist'}, status=status.HTTP_404_NOT_FOUND)

        model_owner_object = ThreeDModel.objects.filter(id=kwargs.get('pk')).first()

        if model_owner_object.owner_id != request.user.id:
            return Response({'error': 'Unauthorized request'}, status=status.HTTP_403_FORBIDDEN)

        return super().destroy(request, *args, **kwargs)


    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            return Response({'error': 'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'], url_path='admin-models', permission_classes=[IsAuthenticated])
    def get_users_models(self, request):
        models = ThreeDModel.objects.filter(owner=request.user)
        serializer = self.get_serializer(models, many=True)
        return Response(serializer.data)

    #get filtering active=true models for main page
    @action(detail=False, methods=['get'], url_path='get-models', permission_classes=[AllowAny], pagination_class=ModelMainPagePagination)
    def get_active_models(self, request):
        try:
            queryset = ThreeDModel.objects.filter(is_active=True)

            for backend in list(self.filter_backends):
                queryset = backend().filter_queryset(request, queryset, self)

            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                usernames = extract_usernames(serializer.data)
                return self.get_paginated_response({
                    "data": serializer.data,
                    "usernames": usernames
            })


            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({'error': 'Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
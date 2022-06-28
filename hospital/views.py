from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination

from hospital.models import Direction, Doctor

from hospital.serializers import (
    DirectionSerializer,
    DoctorSerializer,
    DoctorDetailSerializer,
    DoctorListSerializer,
)


class DirectionViewSet(viewsets.ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class DoctorPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 100


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = DoctorPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["date_birth", "work_experience"]

    @staticmethod
    def _params_to_ints(qs):
        return [int(str_id) for str_id in qs.split(",")]

    def get_queryset(self):
        queryset = self.queryset
        directions = self.request.query_params.get("directions")
        exp_min = self.request.query_params.get("exp_min")
        exp_max = self.request.query_params.get("exp_max")

        if directions:
            directions_ids = self._params_to_ints(directions)
            queryset = queryset.filter(directions__id__in=directions_ids)

        if exp_min:
            queryset = queryset.filter(work_experience__gte=exp_min)

        if exp_max:
            queryset = queryset.filter(work_experience__lte=exp_max)

        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return DoctorListSerializer

        if self.action == "retrieve":
            return DoctorDetailSerializer

        return DoctorSerializer

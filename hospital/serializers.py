from rest_framework import serializers

from hospital.models import (
    Direction,
    Doctor,
)


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = ("id", "direction", "slug", "sort_number")


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = (
            "id",
            "first_name",
            "last_name",
            "slug",
            "directions",
            "description",
            "work_experience",
            "date_birth",
            "sort_number",
        )


class DoctorListSerializer(DoctorSerializer):
    directions = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="direction"
    )


class DoctorDetailSerializer(DoctorSerializer):
    directions = DirectionSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = (
            "id",
            "first_name",
            "last_name",
            "slug",
            "directions",
            "description",
            "work_experience",
            "date_birth",
            "sort_number",
        )

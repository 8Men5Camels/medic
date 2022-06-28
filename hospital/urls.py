from django.urls import path, include
from rest_framework import routers

from hospital.views import (
    DirectionViewSet,
    DoctorViewSet,
)

router = routers.DefaultRouter()
router.register("directions", DirectionViewSet)
router.register("doctors", DoctorViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "hospital"

from django.urls import path, include
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register("contact-us", views.ContactViewSet, basename="contacts")
router.register("membership", views.ApplyViewSet, basename="Memberships")
router.register("orders", views.OrderViewSet, basename="orders")

urlpatterns = [
    path("", include(router.urls))
]

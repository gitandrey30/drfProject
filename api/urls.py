from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ServicesApiView, get_json_warehouse, MadDiesel, WarehouseViewSet, AirPortViewSet,\
    get_person, Super, get_page

from .views import get_categoryes, get_services, get_services_for_title, get_salons, get_json_autos, \
    get_json_condition, get_json_buyer


router = DefaultRouter()
router.register(r'warehouses', WarehouseViewSet, basename='warehouses'),
router.register(r"airport", AirPortViewSet, basename="airport")


urlpatterns = [
    path('categoryes/', get_categoryes),
    path('services/', get_services),
    path('services/<str:title>',get_services_for_title),
    path('salons/', get_salons),
    # path('auto/', get_json_autos),
    path('auto/', MadDiesel.as_view()),
    # path('warehouse/', get_json_warehouse),
    path('condition/', get_json_condition),
    path('buyer/', get_json_buyer),
    path('servicesapiview/',ServicesApiView.as_view()),
    path('', include(router.urls)),
    path('person/', get_person),
    path('person/<int:pk>', get_person),
    path('super/',Super.as_view()),
    # path('air/',AirPortViewSet.as_view()),
    path('celery/', get_page),
]
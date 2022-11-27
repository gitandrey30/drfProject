from django.urls import path

from .views import get_product, get_category

app_name = "drf_work"
urlpatterns = [
    path('api/', get_product),
    path('api_category/', get_category),
    # path("json/", get_person, name="get_json"),
]
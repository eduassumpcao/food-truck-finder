from django.urls import path

from foodtrucks.views import food_truck_map, index

urlpatterns = [
    path("", index, name="index"),
    path("food-truck-map/", food_truck_map, name="food_truck_map"),
]

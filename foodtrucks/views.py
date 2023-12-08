from django.http import HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import render

from foodtrucks.utils.utils import haversine_distance

from .models import FoodTruck


def index(request):
    return render(request, "index.html")


def food_truck_map(request):
    # Get the user's latitude and longitude from the request
    try:
        user_latitude = float(request.GET.get("latitude", 0))
        user_longitude = float(request.GET.get("longitude", 0))
    except ValueError:
        return HttpResponseBadRequest(
            "Invalid latitude or longitude. Please enter valid values."
        )

    # Validate latitude and longitude ranges
    if not (-90 <= user_latitude <= 90) or not (-180 <= user_longitude <= 180):
        return HttpResponseBadRequest(
            "Invalid latitude or longitude. Please enter valid values."
        )

    # Get all food trucks from the database
    all_food_trucks = FoodTruck.objects.all()

    # Check if there are no food trucks
    if not all_food_trucks:
        return HttpResponseBadRequest("No food trucks found.")

    # Calculate distance for each food truck and add it to the queryset
    for truck in all_food_trucks:
        truck.distance = haversine_distance(
            user_latitude, user_longitude, truck.Latitude, truck.Longitude
        )

    # Sort the food trucks by distance
    sorted_food_trucks = sorted(all_food_trucks, key=lambda truck: truck.distance)

    # Check if there are no nearby food trucks
    if not sorted_food_trucks:
        return HttpResponseNotFound("No nearby food trucks found.")

    # Take the first 5 nearest food trucks
    nearest_food_trucks = sorted_food_trucks[:5]

    # Pass the data to the template
    return render(
        request,
        "foodtruck_map.html",
        {
            "customer_coordinates": [user_latitude, user_longitude],
            "food_trucks": [
                {
                    "name": truck.Applicant,
                    "coordinates": [truck.Latitude, truck.Longitude],
                    "address": truck.Address,
                }
                for truck in nearest_food_trucks
            ],
        },
    )

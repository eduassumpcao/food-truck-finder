import pytest
from django.http import HttpResponseBadRequest
from django.test import RequestFactory
from django.urls import reverse

from foodtrucks.models import FoodTruck
from foodtrucks.views import food_truck_map, index


@pytest.fixture
def food_truck(db) -> FoodTruck:
    return FoodTruck.objects.create(
        locationid=123,
        Applicant="Test Truck",
        Address="Test Address",
        Latitude=40.7128,
        Longitude=-74.0060,
    )


@pytest.mark.django_db
def test_index_view():
    # Use the RequestFactory to create a request
    request = RequestFactory().get(reverse("index"))

    # Call the view function
    response = index(request)

    # Assert the response status code
    assert response.status_code == 200


@pytest.mark.django_db
def test_food_truck_map_valid_coordinates(food_truck):
    # Use the RequestFactory to create a request with valid coordinates
    request = RequestFactory().get(
        reverse("food_truck_map"), {"latitude": 37.76873, "longitude": -122.44566}
    )

    # Call the view function
    response = food_truck_map(request)
    print(response.content)
    # Assert the response status code
    assert response.status_code == 200


@pytest.mark.django_db
def test_food_truck_map_invalid_coordinates():
    # Use the RequestFactory to create a request with invalid coordinates
    request = RequestFactory().get(
        reverse("food_truck_map"), {"latitude": "invalid", "longitude": "invalid"}
    )

    # Call the view function
    response = food_truck_map(request)

    # Assert the response status code
    assert response.status_code == 400
    # Assert the response content
    assert isinstance(response, HttpResponseBadRequest)


@pytest.mark.django_db
def test_food_truck_map_no_food_trucks():
    # Use the RequestFactory to create a request
    request = RequestFactory().get(
        reverse("food_truck_map"), {"latitude": 40.7128, "longitude": -74.0060}
    )

    # Call the view function
    response = food_truck_map(request)

    # Assert the response status code
    assert response.status_code == 400
    # Assert the response content
    assert isinstance(response, HttpResponseBadRequest)
    assert b"No food trucks found." in response.content

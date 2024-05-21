import json

import requests, math


def gps_coordinates(city):
    """
    Get the GPS coordinates for a city
    :param city: the city name to search for GPS coordinates
    :return:    the GPS coordinates of the city
    """
    # URL = "https://nominatim.openstreetmap.org/search"
    # params = {"q": city, "format": "json"}
    #
    # response = requests.get(URL, params)
    # result = json.loads(response.content)[0]
    # print(result)
    # if city == "Brisbane":
    #     assert math.isclose(float(result["lat"]), -27.4689682)
    #     assert math.isclose(float(result["lon"]), 153.0234991)
    #
    # return {"latitude": float(result["lat"]), "longitude": float(result["lon"])}
    URL = "https://nominatim.openstreetmap.org/search"
    params = {"q": city, "format": "json"}

    response = requests.get(URL, params)

    result = response.json()[0]  # Parse the JSON data

    if city == "Brisbane":
        assert math.isclose(float(result["lat"]), -27.4689682) , "latitude is not correct"
        assert math.isclose(float(result["lon"]), 153.0234991) ,   "longitude is not correct"

    return {"latitude": float(result["lat"]), "longitude": float(result["lon"])}

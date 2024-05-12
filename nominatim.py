import  requests

def gps_coordinates(city):
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    resp  = requests.get(url)
    data = resp.json()
    #extract the latitude and longitude from the response
    return {"latitude": data[0]["lat"], "longitude": data[0]["lon"]}

    #write assert statements that test the gps_coordinate() function
    assert gps_coordinates("Cairns") ==  {"latitude": "-16.9206455", "longitude": "145.7721854"}, "The GPS coordinates are incorrect"
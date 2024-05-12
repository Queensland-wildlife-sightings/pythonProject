import  requests

def gps_coordinates(city):
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    resp  = requests.get(url)
    data = resp.json()
    # Extract and convertthe latitude and longitude strings into floats 
    # and return a coordinate point 
    return {"latitude": float(data[0]["lat"]), "longitude": float(data[0]["lon"])}

    #write assert statements that test the gps_coordinate() function
    assert gps_coordinates("Cairns") ==  {"latitude": "-16.9206455", "longitude": "145.7721854"}, "The GPS coordinates are incorrect"
    assert gps_coordinates("Sydney") ==  {"latitude": "-33.8548157", "longitude": "151.2164539"}, "The GPS coordinates are incorrect"
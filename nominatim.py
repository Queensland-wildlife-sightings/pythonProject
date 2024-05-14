import json

import  requests

def gps_coordinates(city):
    url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    resp  = requests.get(url)
    result = json.loads(resp.content)
    # Extract and convertthe latitude and longitude strings into floats 
    
    return {"latitude": float(result[0]["lat"]), "longitude": float(result[0]["lon"])}



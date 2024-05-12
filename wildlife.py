import requests

def get_species_list(coordinate,radius):
    url  = f"https://apps.des.qld.gov.au/species/?getspecieslist&kingdom=animals&circle={coordinate},{radius}"
    resp  = requests.get(url)
    #Extract and return the species list. 
    return resp.json()["speciesList"]

# Write assert statements that test the get_species_list() function
assert get_species_list("-16.9206455,145.7721854", 10) == ["Macropus rufus", "Dasyurus maculatus", "Petaurus breviceps"], "The species list is incorrect"
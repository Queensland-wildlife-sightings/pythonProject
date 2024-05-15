<<<<<<< HEAD
import requests
import json

def get_species_list(coordinate,radius):
    url  = f"https://apps.des.qld.gov.au/species/?getspecieslist&kingdom=animals&circle={coordinate},{radius}"
    resp  = requests.get(url)
    #Extract and return the species list. 
    return resp.json()["SpeciesSightingSummariesContainer"]["SpeciesSightingSummary"]["Species"]
=======
import requests,json
>>>>>>> 57c0b68073acaf22a7721109199530efb251fa25


def get_species_list(coordinate, radius ):

    """
    Get the species list from the website.
    args: coordinate: the GPS coordinates of the location
    radius: the radius of the area to search
    """
    lst = []
    url =  "https://apps.des.qld.gov.au/species/"
    params = {"op": "getspecieslist", "kingdom": "animals", "circle": coordinate, "radius": radius}
    resp = requests.get(url,params)
    # Extract and return the species list.
    container=json.loads(resp.content)
    species=container["SpeciesSightingSummariesContainer"]["SpeciesSightingSummary"]
    print(species)
    # for i in range(len(rst["SpeciesSightingSummariesContainer"]["SpeciesSightingSummary"])):
    #     lst =  rst ["SpeciesSightingSummariesContainer"]["SpeciesSightingSummary"][i]["Species"]
    #
    # return lst



def get_survey_by_species(coordinate, radius, taxonid):
    url = f"https://apps.des.qld.gov.au/species/?getsurveysbyspecies&taxonid={taxonid}&circle={coordinate},{radius}"
    rsp = requests.get(url)
    # Extract and return the list of surveys
    return rsp.json()["features"]["properties"]

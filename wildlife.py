import requests
import json

def get_species_list(coordinate,radius):
    url  = f"https://apps.des.qld.gov.au/species/?getspecieslist&kingdom=animals&circle={coordinate},{radius}"
    resp  = requests.get(url)
    #Extract and return the species list. 
    return resp.json()["SpeciesSightingSummariesContainer"]["SpeciesSightingSummary"]["Species"]



# Write assert statements that test the get_species_list() function
 

def get_survey_by_species(coordinate, radius, taxonid):
    url = f"https://apps.des.qld.gov.au/species/?getsurveysbyspecies&taxonid={taxonid}&circle={coordinate},{radius}"
    rsp = requests.get(url)
    # Extract and return the list of surveys
    return rsp.json()["features"]["properties"]
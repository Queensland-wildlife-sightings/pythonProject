import requests, json


def get_species_list(coordinate, radius):
    """
    Get the species list from the website.
    args: coordinate: the GPS coordinates of the location
    radius: the radius of the area to search
    """
    lst = []
    url = "https://apps.des.qld.gov.au/species/"
    params = {"op": "getspecieslist", "kingdom": "animals", "circle": coordinate, "radius": radius}
    resp = requests.get(url, params)

    # Extract and return the species list.
    container = json.loads(resp.content)

    # species = container["SpeciesSightingSummariesContainer"]["SpeciesSightingSummary"]
    # print(species)
    # return the species list
    for species in container["SpeciesSightingSummariesContainer"]["SpeciesSightingSummary"]:
        lst.append(species)

    return lst


def get_survey_by_species(coordinate, radius, taxonid):
    url = f"https://apps.des.qld.gov.au/species/?getsurveysbyspecies&taxonid"
    params = {"op": "getsurveysbyspecies", "taxonid": taxonid, "circle": coordinate, "radius": radius}
    rsp = requests.get(url,params)
   ## retrieve a lis of animal surveys in an area for a given species (taxonid)
    container = json.loads(rsp.content)
    return container["SpeciesSightingSummariesContainer"]["SpeciesSightingSummary"]

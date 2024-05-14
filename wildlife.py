import requests,json


def get_species_list(coordinate, radius ):

    """
    Get the species list from the website.
    args: coordinate: the GPS coordinates of the location
    radius: the radius of the area to search
    """
    lst = []
    url = f"https://apps.des.qld.gov.au/species/?getspecieslist&kingdom=animals&circle={coordinate},{radius}"
    resp = requests.get(url)
    # Extract and return the species list.
    print(resp.content)
    rst =json.loads(resp.content)
    for i in range(len(rst["SpeciesSightingSummariesContainer"][1])):
        lst = lst.append(rst( ["SpeciesSightingSummariesContainer"][1][i][0]))

    return lst



def get_survey_by_species(coordinate, radius, taxonid):
    url = f"https://apps.des.qld.gov.au/species/?getsurveysbyspecies&taxonid={taxonid}&circle={coordinate},{radius}"
    rsp = requests.get(url)
    # Extract and return the list of surveys
    return rsp.json()["features"]["properties"]

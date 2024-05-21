import nominatim
import wildlife


def display_menu():
    print("Help:")
    print("=====")
    print("Display  help                       wildlife> help")
    print("Exit the application                wildlife> exit")
    print("Display animal species in a city    wildlife> species city")
    print("Display animal sightings in a city  wildlife> sightings  1039 Cairns")
    print("Display Venomous species            wildlife> species Cairns venomous")


def filter_venomous(species_list):
    # filter the list of species to only include venomous species
    return [spec for spec in species_list
            if spec['Species']['PestStatus'] == "Venomous"]


def display_sightings(sightings):
    # print the list of animal sightings 
    print("Animal sightings:")

    for sighting in sightings:
        print(
            f"Start Date: {sighting['properties']['StartDate']}, Locality: {sighting['properties']['LocalityDetails']}")


def display_species(species_list):

    print("Species in the city:")
    # display_species(species_list) that prints a list of species to the screen
    # for spec in species_list:
    #     print(
    #         f"Accepted Common Name: {spec['Species']['AcceptedCommonName']},Pest Status: {spec['Species']['PestStatus']}")
    for spec in species_list:
        accepted_common_name = "Unknown "
        pest_status = "Nil"

        if isinstance(spec, dict) and 'Species' in spec:
            species_dict = spec['Species']
            if isinstance(species_dict, dict):
                if 'AcceptedCommonName' in species_dict:
                    accepted_common_name = species_dict['AcceptedCommonName']
                if 'PestStatus' in species_dict:
                    pest_status = species_dict['PestStatus']

        print(f"Accepted Common Name: {accepted_common_name}, Pest Status: {pest_status}")


def main():
    while True:
        command = input("wildlife> ")
        input_commands = command.split(" ")

        if len(command) == 0:
            print("Please enter a command or type help for a list of commands.")

        elif "help" in input_commands:  # [0] == "help":

            display_menu()

        elif input_commands[0] == "species":
            if len(input_commands) > 1:
                city = input_commands[1]
                if len(input_commands) > 2 and input_commands[2] == "venomous":
                    spc_list = search_species(city)
                    venomous_list = filter_venomous(spc_list)

                    assert len(venomous_list) == 0, "The list is empty"
                    # Test if the venomous list contains non-venomous species

                    # test the filter function to return a list of venomous species
                    assert len(venomous_list) != 0, "The list is empty"

                    # Test if the venomous list contains non-venomous species
                    for spec in venomous_list:
                        assert spec['Species']['PestStatus'] == "Venomous", "contain non venomous species"

                    display_species(venomous_list)
                else:
                    spc_list = search_species(city)
                    display_species(spc_list)

        elif input_commands[0] == "sightings":
            if len(input_commands) > 2:
                toxonid = input_commands[1]
                city = input_commands[2]
                sightings_list = search_sightings(toxonid, city)
                display_sightings(sightings_list)

        elif command == "exit":
            break
        else:
            print("Invalid command. Type 'help' for a list of commands.")


def search_sightings(toxonid, area):
    """
    function to search the sightings of the species in the area
    :param toxonid: the species id
    :param area: the area that user want to search for sightings
    :return: the list of sightings in the area
    """
    coordin = gps(area)

    RADIUS = 100000
    sighting_lst = wildlife.get_survey_by_species(coordin, RADIUS, toxonid)

    #Filter out the sightings by choosing only those surveys for which the SiteCode is INCIDENTAL.
    sighting_lst = [sighting for sighting in sighting_lst if sighting['properties']['SiteCode'] == "INCIDENTAL"]

    return sighting_lst # return the list of sightings

    # return [
    #     {"properties": {"StartDate": "2021-01-01", "LocalityDetails": "Cairns"}},
    #     {"properties": {"StartDate": "2021-01-02", "LocalityDetails": "Brisbane"}}]


def search_species(city):
    """
    function to search the species of the city
    :param city: city that user want to search for species
    :return:  the list of  species in the city
    """
    coordin = gps(city)

    RADIUS = 100000
    spec_lst = wildlife.get_species_list(coordin, RADIUS)

    return spec_lst

    # return [
    #     {"Species":{"AcceptedCommonName":"dolphin", "PestStatus":"Nil"}},
    #     {"Species":{"AcceptedCommonName":"snake","PestStatus":"Venomous"}}]


def gps(city):
    # return the GPS coordinates for a city
    # return {"latitude": -27.4689682, "longitude": 153.0234991 }

    nominatim.gps_coordinates(city)


main()



import nominatim
def display_menu():
    print("Help:")
    print("=====")
    print("Display  help                       wildlife> help")
    print("Exit the application                wildlife> exit")
    print("Display animal species in a city    wildlife> species city")
    print("Display animal sightings in a city  wildlife> sightings Cairns 1039")
    print("Display Venomous species            wildlife> species Cairns venomous")


def filter_venomous(species_list):
    # filter the list of species to only include venomous species
    return [spec for spec in species_list
            if spec['Species']['PestStatus'] == "Venomous"]
    # add asserts to check the function
    assert (specie_list == {}) or (specie_list == []), "The list is empty"
    assert (spec for spec in species_list)
    [isinstance(spec, list), "not list type"]


def display_sightings(sightings):
    # print the list of animal sightings 
    print("Animal sightings:")

    for sighting in sightings:
        print(
            f"Start Date: {sighting['properties']['StartDate']}, Locality: {sighting['properties']['LocalityDetails']}")


def display_species(species_list):
    print("Species in the city:")
    # display_species(species_list) that prints a list of species to the screen
    for spec in species_list:
        print(
            f"Accepted Common Name: {spec['Species']['AcceptedCommonName']},Pest Status: {spec['Species']['PestStatus']}")


def main():
    while True:
        command = input("wildlife> ")
        input_commands = command.split(" ")

        if command == "help":
            display_menu()

        elif input_commands[0] == "species":
            if len(input_commands) > 1:
                city = input_commands[1]
                if len(input_commands) > 2 and input_commands[2] == "venomous":
                    spc_list = search_species(city)
                    venomous_list = filter_venomous(spc_list)
                    display_species(venomous_list)
                else:
                    spc_list = search_species(city)
                    display_species(spc_list)

        elif input_commands[0] == "sightings":
            if len(input_commands) > 2:
                species = input_commands[1]
                city = input_commands[2]
                sightings_list = search_sightings(species, city)
                display_sightings(sightings_list)

        elif command == "exit":
            break

        # Update main() to accept the command “sightings” followed by a species, a comma and an
        # area. When this command is received, use the search_sightings(species,area) and
        # display_sightings(sightings) functions to display a list of sightings to the user.


def search_sightings(species, area):
    return [{"properties": {"StartDate": "1999-11-15",
                            "LocalityDetails": "Tinaroo"}}]


def search_species(city):
    gps(city)
    return [
        {"Species": {"AcceptedCommonName": "dolphin",
                     "PestStatus": "Nil"}},

        {"Species": {"AcceptedCommonName": "snake",
                     "PestStatus": "Venomous"}}
    ]


def sear_species(taxonid, city):
    #  return a fixed list of animal sightings
    return [{"properties": {"StartDate": "1999-11-15",
                            "LocalityDetails": "Tinaroo"}}]

def gps(city):
    # return the GPS coordinates for a city
    return {"latitude": -27.4689682, "longitude": 153.0234991 }

    #Add assert statement(s) to check that Brisbane returns the correct GPS coordinate
    assert gps("Brisbane") == {"latitude": -27.4689682, "longitude": 153.0234991}, "The GPS coordinates are incorrect"


main()

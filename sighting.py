def display_menu():
    print("Help:")
    print("=====")
    print("Display  help                       wildlife> help")
    print("Exit the application                wildlife> exit")
    print("Display animal species in a city    wildlife> species city")
    print("Display animal sightings in a city  wildlife> sightings Cairns 1039")
    print("Display Venomous species            wildlife> species Cairns venomous")


def venomous_display():
    pass


def filter_venomous(species_list):
    #fiter to choice the Venomous
    return [species for species in species_list 
            if species['Species']['PestStatus'] == 'Venomous']


def display_sightings(sightings):
    # print the list of animal sightings 
    
    for sighting in sightings:
        print(f"Start Date: {sighting['properties']['StartDate']}, Locality: {sighting['properties']['LocalityDetails']}")


def display_species(species_list):
    #display each species in the list
    for species in species_list:
        print(f"Species: {species['Species']['AcceptedCommonName']},
                Pest Status: {species['Species']['PestStatus']}")

def main():
    while True:
        city = input("wildlife> species city")
        command = input("wildlife> ")
        if command == "help":
            display_menu()
        if command == input("wildlife> species city"):
            search_species(city)
           # display_species(species_list)

        if command == input("wildlife> species Cairns venomous"):
            pass


        if command == input("wildlife> sightings"):
        # Update main() to accept the command “sightings” followed by a species, a comma and an
        # area. When this command is received, use the search_sightings(species,area) and
        # display_sightings(sightings) functions to display a list of sightings to the user.
            pass



        elif command == "exit":
            break


def search_sightings(species, area):
    return [{"properties": {"StartDate": "1999-11-15", "LocalityDetails": "Tinaroo"}}]

def search_species(city):
    return [
        {"Species":{"AcceptedCommonName":"dolphin", "PestStatus":"Nil"}},
        {"Species":{"AcceptedCommonName":"snake","PestStatus":"Venomous"}}
    ]
def search_species(taxonid, city):
    #  return a fixed list of animal sightings
    return [{"properties": {"StartDate": "1999-11-15", 
                            "LocalityDetails": "Tinaroo"}}]


main()

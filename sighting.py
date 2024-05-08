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


def display_sightings(sightings):
    pass

def display_species(species_list):
    pass

def main():
    

    while True:
    
         
        command = input("wildlife> ")
        input_commands = command.split(" ")
        

        if len(input_commands) == 0 and command =="help" :
        #if command == "help":
            display_menu()

        # elif len(input_commands) == 0 and input_commands[0] == "exit":
        #     break
        elif input_commands[0] == "species":
            if len(input_commands) > 1:
                city  = input_commands[1]
                #print(city)
                 
                spc_list = search_species(city)
                display_species(spc_list)

     


        
        # Update main() to accept the command “sightings” followed by a species, a comma and an
        # area. When this command is received, use the search_sightings(species,area) and
        # display_sightings(sightings) functions to display a list of sightings to the user.
            



        elif command == "exit":
            break


def search_sightings(species, area):
    return [{"properties": {"StartDate": "1999-11-15", "LocalityDetails": "Tinaroo"}}]

def search_species(city):
    return [
        {"Species":{"AcceptedCommonName":"dolphin", "PestStatus":"Nil"}},
        {"Species":{"AcceptedCommonName":"snake","PestStatus":"Venomous"}}
    ]
# def search_species(taxonid, city):
#     pass


main()

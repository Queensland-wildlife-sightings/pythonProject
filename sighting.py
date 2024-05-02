def display_menu():
    print("Help:")
    print("=====")
    print("Display  help                   wildlife> help")
    print("Exit the application            wildlife> exit")


def main():
    while True:
        command = input("wildlife> ")
        if command == "help":
            display_menu()
        elif command == "exit":
            break


main()
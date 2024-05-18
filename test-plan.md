Test Plan reports

	Debug and document your main() function.\
This photo indicates the error of input led to not return the correct item.

![Task_main()_error1](https://github.com/Queensland-wildlife-sightings/Intro-To-Programming-Assignment2/assets/162095163/ef16cb5a-8b29-4467-b9dd-62c73d2f8b29)

The following photo shows the result after fixing the “elif” statement. The results shows when inputting the correct command will correctly execute the mani().
 
![Task3_main()_debug2](https://github.com/Queensland-wildlife-sightings/Intro-To-Programming-Assignment2/assets/162095163/0c507ec2-7ef2-44b1-85ee-1a0dd7b9b63a)


 
Tast5  Test Plan: Venomous Species Filtering
Function: filter_venomous
Description: Test whether the filter_venomous function correctly filters venomous species.

Input:
Python

[
    {"Species": {"AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
    {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}},
    {"Species": {"AcceptedCommonName": "spider", "PestStatus": "Venomous"}},
    {"Species": {"AcceptedCommonName": "lizard", "PestStatus": "NonVenomous"}}
]
Expected Output:
Python

[
    {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}},
    {"Species": {"AcceptedCommonName": "spider", "PestStatus": "Venomous"}}
]

Test Steps:
Call the filter_venomous function with the provided input.
Verify that the output matches the expected result.
Assertions:
Ensure that the number of venomous species in venomous_list is 2.
Check that each species in venomous_list is labeled as “Venomous.”
Function: Display Menu
Description: Test whether the display_menu function correctly displays menu options.

Input: None
Expected Output:
1. Search species in a city
2. Display venomous species
3. Exit

Test Steps:
Call the display_menu function.
Verify that the screen output matches the expected result.
Function: Search Species
Description: Test whether the search_species function returns the expected list of species.

Input:
Python
[
    {"Species": {"AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
    {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}},
    {"Species": {"AcceptedCommonName": "spider", "PestStatus": "Venomous"}},
    {"Species": {"AcceptedCommonName": "lizard", "PestStatus": "NonVenomous"}}
]

"Brisbane"
Expected Output:
Python

[
    {"Species": {"AcceptedCommonName": "dolphin", "PestStatus": "Nil"}},
    {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}},
    {"Species": {"AcceptedCommonName": "spider", "PestStatus": "Venomous"}},
    {"Species": {"AcceptedCommonName": "lizard", "PestStatus": "NonVenomous"}}
]
Test Steps:
Call the search_species function with the provided input.
Verify that the output matches the expected result.
  

Test Plan reports

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
AI-generated code. Review and use carefully. More info on FAQ.
Expected Output:
Python

[
    {"Species": {"AcceptedCommonName": "snake", "PestStatus": "Venomous"}},
    {"Species": {"AcceptedCommonName": "spider", "PestStatus": "Venomous"}}
]

AI-generated code. Review and use carefully. More info on FAQ.
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
AI-generated code. Review and use carefully. More info on FAQ.
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

![Task5_Test1_result_sucess](https://github.com/Queensland-wildlife-sightings/Intro-To-Programming-Assignment2/assets/162095163/50e856b9-4802-40b8-b48f-9a113d784562)
![Task5_Test1_result_error](https://github.com/Queensland-wildlife-sightings/Intro-To-Programming-Assignment2/assets/162095163/b21588d8-a6f5-4750-bad0-7122d58c27b8)


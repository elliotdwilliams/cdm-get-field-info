'''
Queries the CONTENTdm Server API for a list of all collections in a repository,
then downloads the field information for each collection as an XML file.
'''

import os.path
import requests

# Set directory to save files, and check it exists
directory = "./field_data"
if not os.path.isdir(directory):
    os.mkdir(directory)

# Set base URL to CONTENTdm website URL
BASE_URL = "https://digital.utsa.edu"

# Make an API request to get collection list
collection_list_url = BASE_URL + "/digital/bl/dmwebservices/index.php?q=dmGetCollectionList/json"
collection_response = requests.get(collection_list_url, timeout=5)

# Create an empty list to hold collection aliases
alias_list = []

# Loop through collection list and add alias to list
for collection in collection_response.json():
    alias = collection["alias"].lstrip("/")
    # print(alias)
    alias_list.append(alias)

# Save collection list to directory
file_name = os.path.join(directory, "collection_list.txt")
s = "\n".join(alias_list)
with open(file_name, mode="w") as f:
    f.write(s)

# Alternate method: Open a file to get the list of collection aliases, then split that list into separate lines
# alias_list = open("alias-test.txt", "r", encoding="utf-8").readlines()

# Loop through each line in the list of aliases
for line in alias_list:
    alias = line.rstrip()
    print(alias)

    # Make an API request for the collection
    collection_url = BASE_URL + "/digital/bl/dmwebservices/index.php?q=dmGetCollectionFieldInfo/" + alias + "/xml"
    response = requests.get(collection_url, timeout=5)
    print(response.status_code)  # Print status code for error checking

    # Save the request output to file
    file_name = os.path.join(directory, (alias + ".xml"))
    with open(file_name, mode="w", encoding="utf-8") as f:
        f.write(response.text)

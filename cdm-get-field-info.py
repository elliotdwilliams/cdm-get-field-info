import requests

# Open a file to get the list of collection aliases, then split that list into separate lines
alias_list = open("alias-test.txt", "r", encoding="utf-8").readlines()

# Loop through each line in the list of aliases
for line in alias_list:
    alias = line.rstrip()
    print(alias)

    # Make an API request for the collection
    collection_url = "https://digital.utsa.edu/digital/bl/dmwebservices/index.php?q=dmGetCollectionFieldInfo/" + alias + "/xml"
    response = requests.get(collection_url)
    print(response.status_code)

    # Save the request output to file
    with open(alias + ".xml", mode="w", encoding="utf-8") as f:
        f.write(response.text)
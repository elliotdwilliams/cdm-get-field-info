# cdm-get-field-info

Simple python script for quickly downloading the field information for every collection in a CONTENTdm repository.  The field information contains information about how each metadata field in a collection is configured.

The script queries the CONTENTdm API to get a list of all collections in the repository, then makes queries for each collection's field information. The field info for each collection is saved as a separate XML file, with the collection alias as the filename.

Uses the dmwebservices wrapper for the CONTENTdm Server API: https://help.oclc.org/Metadata_Services/CONTENTdm/Advanced_website_customization/API_Reference/CONTENTdm_API/CONTENTdm_Server_API_Functions_dmwebservices

To use the script with a different CONTENTdm site, change the "base_URL" variable to the desired CONTENTdm URL.

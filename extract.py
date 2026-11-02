# Import python library to extract data from an API
import requests
url = "https://www.fema.gov/api/open/v2/PublicAssistanceFundedProjectsDetails"
api_data = requests.get(url)
## display first 3 rows of the data based on column public assitance. Identify the data by its your datatype
print(api_data.json()['PublicAssistanceFundedProjectsDetails'][:3])

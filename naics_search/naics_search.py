import json
import os
from django.conf import settings

def load_naics_data():
    file_path = os.path.join(settings.BASE_DIR, 'api', 'naics_search', 'data', 'naics2017.json')
    with open(file_path, 'r') as f:
        return json.load(f)

NAICS_DATA = load_naics_data()

def search_naics(query):
    results = []
    if query.isdigit():
        # If the query is numeric, search in 'Code'
        results = [code for code in NAICS_DATA if query in code['Code']]
    else:
        # If the query is not numeric, search in 'Class Title' and 'Element Description English'
        results = [code for code in NAICS_DATA if query.lower() in code['Class Title'].lower() or query.lower() in code['Element Description English'].lower()]
    
    # Limit the number of results to 20
    return results[:100]

### Number search algorithm different. Below search, numbers has to exact match.
# def search_naics(query):
#     results = []
#     if query.isdigit():
#         # If the query is numeric, search in 'Code'
#         results = [code for code in NAICS_DATA if code['Code'].startswith(query)]
#     else:
#         # If the query is not numeric, search in 'Class Title' and 'Element Description English'
#         results = [code for code in NAICS_DATA if query.lower() in code['Class Title'].lower() or query.lower() in code['Element Description English'].lower()]
    
#     # Limit the number of results to 20
#     return results[:20]

import requests
from pprint import pprint
import pandas as pd

###############################################
api_key = "4b60d0ae-509a-40ca-adb9-445033fac7e5"
from_date = "1900-03-04"
to_date = "2022-03-05"
order_by = "oldest" 
show_fields = "all"
page_size = "1"
section = "politics"




#"bodyText,firstPublicationDate,headline"

query_url = "http://content.guardianapis.com/search?" \
            f"from-date={from_date}" \
            f"&to-date={to_date}" \
            f"&section={section}" \
            f"&order-by={order_by}" \
            f"&show-fields={show_fields}" \
            f"&page-size={page_size}" \
            f"&api-key={api_key}"             
            

r = requests.get(query_url)
pprint(r.json())
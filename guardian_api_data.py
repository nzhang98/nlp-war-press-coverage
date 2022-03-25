import requests
import pandas as pd
import datetime
import time
import pandas as pd
from pprint import pprint

def getCall(query = "search", 
            api_key = "4b60d0ae-509a-40ca-adb9-445033fac7e5",
            from_date = "1900-01-01",
            to_date = datetime.datetime.today().strftime("%Y-%m-%d"),
            order_by = "oldest",
            page_size = 200,
            page = 1,
            section = "politics",
            show_fields = "all",
            q_filter = None,
            query_fields = "body,headline"):
    
    if query == "search":
        pass

    query_url = "http://content.guardianapis.com/search?" \
            f"from-date={from_date}" \
            f"&to-date={to_date}" \
            f"&section={section}" \
            f"&order-by={order_by}" \
            f"&show-fields={show_fields}" \
            f"&page-size={page_size}" \
            f"&api-key={api_key}"  \
            f"&q={q_filter}" \
            f"&query-fields={query_fields}" \
            f"&page={page}"

    return requests.get(query_url).json()

def saveData(query = "search", 
            api_key = "4b60d0ae-509a-40ca-adb9-445033fac7e5",
            from_date = "1900-01-01",
            to_date = datetime.datetime.today().strftime("%Y-%m-%d"),
            order_by = "oldest",
            page_size = 200,
            page = 1,
            section = "politics",
            show_fields = "all",
            q_filter = None,
            query_fields = "body,headline"
            ):
    n_pages = getCall(query = query, api_key = api_key, from_date = from_date, to_date = to_date,
                order_by = order_by, page_size = page_size, page = page, section = section,
                show_fields = show_fields, q_filter = q_filter, query_fields = query_fields)['response']['pages']
    print(int(n_pages))

    df = pd.DataFrame()
    for currentPage in range(1, n_pages):
        print("Page: ", currentPage, "/", n_pages)
        try: 
            r = getCall(query = query, api_key = api_key, from_date = from_date, to_date = to_date,
                    order_by = order_by, page_size = page_size, page = currentPage, section = section,
                    show_fields = show_fields, q_filter = q_filter, query_fields = query_fields)['response']['results']
        except:
            print('Problem with page: ', currentPage)
            continue

        for i in range(len(r)):
            article = pd.DataFrame(r[i]['fields'], index = [0])
            df = pd.concat([df, article], ignore_index = True)

        time.sleep(1)

    return df

api_key = "4b60d0ae-509a-40ca-adb9-445033fac7e5"
from_date = "1900-01-01"
to_date = datetime.datetime.today().strftime("%Y-%m-%d")
order_by = "oldest" 
page_size = "200"
page = 111
section = "politics"
show_fields = "bodyText,headline,newspaperEditionDate,webPublicationDate,firstPublicationDate"
q_filter = '"war" OR "warfare" OR "conflict"'
query_fields = "body,headline"

r = getCall(from_date = from_date, page = page, order_by = "oldest", 
            page_size = 200, show_fields = show_fields, q_filter = q_filter, query_fields = query_fields)

r = r['response']['results']
for i in range(len(r)):
    article = pd.DataFrame(r[i]['fields'], index = [0])
    df = pd.concat([df, article], ignore_index = True)

df = saveData(api_key = api_key,
        from_date = from_date, 
        to_date = to_date,
        order_by = order_by, 
        page_size = page_size, 
        page = page, 
        section = section,
        show_fields = show_fields, 
        q_filter = q_filter, 
        query_fields = query_fields)

#redo pages: 90, 111

# df.to_csv('/datasets/guardian_dataset_raw.csv')
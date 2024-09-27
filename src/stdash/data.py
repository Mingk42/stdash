import requests as reqs

##################################################################
def load_data():
    url = "http://43.202.66.118:8077/all"

    resp = reqs.get(url)
    data = resp.json()

    return data
##################################################################
import requests as reqs
import os

##################################################################
def load_data():
    url = "http://43.202.66.118:8077/all"

    resp = reqs.get(url)
    data = resp.json()

    return data
##################################################################



def font_path():
    font_path = os.path.dirname(os.path.abspath(__file__))

    return f"{font_path}/fonts/NanumSeongsil.ttf"
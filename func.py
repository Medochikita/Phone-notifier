import requests
import json

def make_request(name = None, body = None, web_url = None, image = False):
    with open("/home/pi/Desktop/main_passwords.json", "r") as f:
        if image == False:
            url = json.load(f)["IFTTT_urls"]["url_web"]
        else:
            url = json.load(f)["IFTTT_urls"]["url_image"]

    if web_url == None:
        data = {"value1": f"{name}", "value2": f"{body}"}
    else:
        data = {"value1": f"{name}", "value2": f"{body}", "value3": f"{web_url}"}
        
    requests.post(url=url, json=data)
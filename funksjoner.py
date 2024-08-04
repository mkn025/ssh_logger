import re
import requests
import datetime
from json import load
from os import system, path


def load_json_file(file):
    with open(file, "r") as file:
        return load(file)
    

def append_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text)


def hent_linjer(filename,n,start=False):
    with open(filename, "r") as file:
        lines = file.readlines()
        if start:
            return lines[n]
        else:
            return(lines[-n:])



def find_ip_addresses(input_string):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ip_addresses = re.findall(ip_pattern, input_string)
    return ip_addresses


def dato_og_tid():
    now = datetime.datetime.now()
    formatted_time = now.strftime("%m/%d/%Y %I:%M %p")
    return formatted_time



def get_ip_info_location(ip_address):
    adress = f"https://api.iplocation.net/?cmd=ip-country&ip={ip_address}"
    r = requests.get(adress)
    return r.json()["country_name"]




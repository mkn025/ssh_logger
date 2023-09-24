import re
import datetime
def hent_linjer(filename,n,start=False):
    with open(filename, "r") as file:
        lines = file.readlines()
        if start:
            return lines[n]
        else:
            return(lines[-n:])

def append_to_file(filename, text):
    with open(filename, "a") as file:
        file.write(text + "\n")


def find_ip_addresses(input_string):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ip_addresses = re.findall(ip_pattern, input_string)
    return ip_addresses


def dato_og_tid():
    now = datetime.datetime.now()
    formatted_time = now.strftime("%m/%d/%Y %I:%M %p")
    return formatted_time

    
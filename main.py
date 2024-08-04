from funksjoner import *
import time


# variables
config_file = load_json_file("conf/conf.json")
output_file = config_file["output_file"] if len(config_file["output_file"]) > 0 else "logg.txt"
logg_tester = None
antall_ganger_kjørt = 0 

while True:
    try:
        updates = int(config_file['update'])
        amount_of_lines = int(config_file['linjer'])
        print(f"start time {dato_og_tid()}") and append_to_file(output_file, dato_og_tid()) if antall_ganger_kjørt == 0 else None
        print(f"program updates every {updates} sek og writes lines {amount_of_lines} to file")
    except:
        print(f"start time {dato_og_tid()}") and append_to_file(output_file, dato_og_tid()) if antall_ganger_kjørt == 0 else None
        updates = 5
        amount_of_lines = 1
        print("conf.json was not found")
    logg = hent_linjer("/var/log/auth.log", amount_of_lines)
    if logg == logg_tester:
        pass
    else:
        for n in logg:
            append_to_file(f"{output_file}",n)
            ip_adresse = find_ip_addresses(n)
            append_to_file(f"ip_{output_file}",f"ip adresse: {ip_adresse[0]} <==> {dato_og_tid()} Location <==> {get_ip_info_location(ip_adresse[0])}") if len(ip_adresse) > 0 else None
        antall_ganger_kjørt += 1
     
    logg_tester = logg 
    time.sleep(updates)












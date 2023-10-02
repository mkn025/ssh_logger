from funksjoner import *
import time

logg_tester = None
antall_ganger_kjørt = 0 
while True:
    antall_ganger_kjørt += 1
    try:
        updates = int(hent_linjer("conf/etc.conf",1,True))
        amount_of_lines = int(hent_linjer("conf/etc.conf",3,True))
        print(f"program updates every {updates} sek og writes lines {amount_of_lines} to file")
        print(f"start time {dato_og_tid()}") if antall_ganger_kjørt < 0 else None
    except:
        print(f"start time {dato_og_tid()}") if antall_ganger_kjørt < 0 else None
        updates = 5
        amount_of_lines = 1
        print("etc.conf was not found")
    logg = hent_linjer("/var/log/auth.log", amount_of_lines)
    if logg == logg_tester:
        pass
    else:
        for n in logg:
            append_to_file("logg/logg.txt",n)
            ip_adresse = find_ip_addresses(n)
            append_to_file("logg/logg_ip.txt",f"ip adresse: {ip_adresse[0]} <==> {dato_og_tid()}") if len(ip_adresse) > 0 else None
            
    logg_tester = logg
    time.sleep(updates)












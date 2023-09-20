from funksjoner import *
import time

log_tester = None

while True:
    try:
        oppdateringer = int(hent_linjer("etc.conf",1,True))
        antall_linjer = int(hent_linjer("etc.conf",3,True))
        print(f"program kjører med {oppdateringer} sek og skrver {antall_linjer} linjer til fil")
    except:
        oppdateringer = 5
        antall_linjer = 1
        print("fant ikke fil")
    log = hent_linjer("/var/log/auth.log", antall_linjer)
    if log == log_tester:
        pass
    else:
        for n in log:
            append_to_file("logg.txt",n)
            ip_adresse = find_ip_addresses(n)
            append_to_file("logg_ip.txt",f"ip adresse: {ip_adresse[0]}") if len(ip_adresse) > 0 else None
    log_tester = log
    time.sleep(oppdateringer)












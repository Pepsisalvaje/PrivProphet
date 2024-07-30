import argparse
import requests

def listsuid(lista):
    print("Revisando la Lista...")


def uniquesuid(suid):
    print(f"Revisando el SUID {suid}...")

    url = f'https://gtfobins.github.io/gtfobins/{suid}/#sudo'
    
    # Realizar la solicitud a la página
    print(url)
    response = requests.get(url)

    if response.status_code == 200:
        print(f"SUID {suid} is vulnerable")
    else:
        print(f"SUID {suid} is not vulnerable")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Descripción de tu programa")

    # Agregar argumentos
    parser.add_argument('-l', '--list', help='List of SUID')
    parser.add_argument('-s', '--suid', help='SUID to check')

    # Parsear los argumentos
    args = parser.parse_args()

    if args.suid:
        uniquesuid(args.suid)

    if args.list:
        listsuid(args.list)
    

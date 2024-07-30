import argparse

def listsuid(lista):
    print("Revisando la Lista...")


def uniquesuid(suid):
    print(f"Revisando el SUID {suid}...")


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
    

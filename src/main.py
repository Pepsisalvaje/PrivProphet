import argparse
import requests
from bs4 import BeautifulSoup
import re

def listsuid(lista):
    print("Revisando la Lista...")

def findsuid(suid):
    url = f'https://gtfobins.github.io/gtfobins/{suid}/#sudo'
    
    # Realizar la solicitud a la página
    #print(url)
    response = requests.get(url)

    if response.status_code == 200:
        print(f"SUID {suid} is vulnerable")
        print("\n")
        soup = BeautifulSoup(response.content, 'html.parser')
        h2 = soup.find('h2', id='sudo')
        #ul_examples = soup.find('ul', class_='examples')
        
        if h2:
            # Buscar el siguiente hermano del h2 que sea un ul
            ul = h2.find_next_sibling('ul')

            

            ul = str(ul)

            ul = ul.replace('<ul class="examples">',"")
            ul = ul.replace('<li>',"")
            ul = ul.replace('<p>',"")
            ul = ul.replace('</p>',"")
            ul = ul.replace('</li>',"")
            ul = ul.replace('</code>',"")
            ul = ul.replace('</div>',"")
            ul = ul.replace('</ul>',"")
            ul = re.sub(r'<a\s+href="[^"]*">(.*?)</a>', r'\1' , ul, flags=re.DOTALL)
            ul = re.sub(r'<div[^>]*>', '' , ul, flags=re.DOTALL)
            ul = re.sub(r'<code[^>]*>', '' , ul, flags=re.DOTALL)
            
            #ul = re.sub(r'<p[^>]*>(.*?)</p>', r'\1', ul, flags=re.DOTALL)

            #ul = re.sub(r'<a\s+code="[^"]*">(.*?)</code>', r'\1' , ul, flags=re.DOTALL)

            print(ul)


        else:
            print('No se encontró el elemento <h2> con id "7z".')
    else:
        print(f"SUID {suid} is not vulnerable")

def uniquesuid(suid):
    findsuid(suid)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Program Description")

    # Agregar argumentos
    parser.add_argument('-l', '--list', help='List of SUID')
    parser.add_argument('-s', '--suid', help='SUID to check')

    # Parsear los argumentos
    args = parser.parse_args()

    if args.suid:
        uniquesuid(args.suid)

    if args.list:
        listsuid(args.list)
    

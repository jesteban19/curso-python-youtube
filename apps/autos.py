import requests
from bs4 import BeautifulSoup

url = "https://www.gta5rides.com/vehicles/compacts.cfm"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    vehiculos = soup.find_all("div",{"class":"card-body"})
    print("Lista de autos de GTA V: \n")
    for vehiculo in vehiculos:
        nombre = vehiculo.find_all("span")
        if nombre:
            print(f"- {nombre[1].text}")
    
else:
    print("Error al acceder a la pagina:",response.status_code)
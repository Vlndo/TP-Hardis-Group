import requests
import argparse
import time

# Premier exo :
def http_get() -> dict : 
    r = requests.get('https://dummyjson.com/products')
    print("------------------------Début EXO 1--------------------------")
    print(f"Code de retour obtenu : {r.status_code}")
    if r.status_code != 200: # si le r.status_code est différent de 200 alors on affiche le message d'erreur suivant et le code d'erreur
        raise Exception(f"Erreur HTTP : {r.status_code}")
    return r.json()

data = http_get()
print(f"Nombre de retour pour la requete get : {len(data['products'])}")
print("------------------------Fin EXO 1--------------------------")


# Deuxième exo
def parse_command_line_args():

    parser = argparse.ArgumentParser()
    parser.add_argument("--protocol", type= str, choices= ['http', 'https'], required= True) #on dit ici que l'on veut uniquement les protocoles Http et Https
    parser.add_argument("--hostname", type= str, required= True) # comme pour protocol hostname doit etre de type String
    parser.add_argument("--uri", type= str, required= True)
    parser.add_argument("--threshold", type= int, required= True)

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_command_line_args()
    print("------------------------Début EXO 2--------------------------")
    print(f"Protocol : {args.protocol}")
    print(f"Hostname : {args.hostname}")
    print(f"URI : {args.uri}")
    print(f"Threshold : {args.threshold}")
    print("------------------------Fin EXO 2--------------------------")


# Exo 3
def format_url(protocol:str, hostname:str, uri:str) -> str:
    if protocol not in ("http", "https"):
        raise Exception(f"Protocole invalide : {protocol} est différent de http ou https")
    
    if not hostname or " " in hostname:
        raise Exception(f"Hostname invalide : '{hostname}'")
    
    if not uri.startswith("/"):
        raise Exception(f"Uri invalide : doit commencé par un '/'")
    
    url = f"{protocol}://{hostname}{uri}"

    return url
print("------------------------Début EXO 3--------------------------")
print(f'Url final : {format_url("https","google.com","/fr")}')
print("------------------------Fin EXO 3--------------------------")

# Exo 5
def http_get_V2(url:str) -> dict : 
    r = requests.get(url)
    print("------------------------Début EXO 1--------------------------")
    print(f"Code de retour obtenu : {r.status_code}")
    if r.status_code != 200: # si le r.status_code est différent de 200 alors on affiche le message d'erreur suivant et le code d'erreur
        raise Exception(f"Erreur HTTP : {r.status_code}")
    return r.json()

if __name__ == "__main__":
    data = http_get_V2("https://dummyjson.com/products")
    print(f"Nombre de retour pour la requete get : {len(data['products'])}")
    print("------------------------Fin EXO 5--------------------------")

# Exo 6 
class ThresholdExceededException(Exception):

    def __init__(self, threshold: int, actual: float):
        self.threshold = threshold
        self.actual = actual
        super().__init__(f"Temps d'exécution de {actual:.2f}s dépassé (seuil: {threshold}s).")


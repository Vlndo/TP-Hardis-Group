import requests
import argparse
import time
import logging

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

# if __name__ == "__main__":
#     args = parse_command_line_args()
#     print("------------------------Début EXO 2--------------------------")
#     print(f"Protocol : {args.protocol}")
#     print(f"Hostname : {args.hostname}")
#     print(f"URI : {args.uri}")
#     print(f"Threshold : {args.threshold}")
#     print("------------------------Fin EXO 2--------------------------")


# Exo 3
def format_url(protocol:str, hostname:str, uri:str) -> str:
    if protocol not in ("http", "https"):
        raise Exception(f"Protocole invalide : {protocol} est différent de http ou https")
    
    if not hostname or " " in hostname:
        raise Exception(f"Hostname invalide : '{hostname}'")
    
    if not uri.startswith("/"):
        raise Exception("Uri invalide : doit commencé par un '/'")
    
    url = f"{protocol}://{hostname}{uri}"

    return url
print("------------------------Début EXO 3--------------------------")
print(f'Url final : {format_url("https","google.com","/fr")}')
print("------------------------Fin EXO 3--------------------------")

# Exo 5
def http_get_V2(url:str) -> dict : 
    r = requests.get(url)
    print("------------------------Début EXO 5--------------------------")
    print(f"Code de retour obtenu : {r.status_code}")
    if r.status_code != 200: # si le r.status_code est différent de 200 alors on affiche le message d'erreur suivant et le code d'erreur
        raise Exception(f"Erreur HTTP : {r.status_code}")
    return r.json()

# if __name__ == "__main__":
#     data = http_get_V2("https://dummyjson.com/products")
#     print(f"Nombre de retour pour la requete get : {len(data['products'])}")
#     print("------------------------Fin EXO 5--------------------------")

# Exo 6 
class ThresholdExceededException(Exception):

    def __init__(self, threshold: int, actual: float):
        self.threshold = threshold
        self.actual = actual
        super().__init__(f"Temps d'exécution de {actual:.2f}s dépassé (seuil: {threshold}s).")

# # Exo 7
# def fetch_with_threshold(url: str, threshold: int):
#     start_time = time.time()

#     try:
#         response = requests.get(url)

#     except Exception as context:
#         print("Erreur lors de la requête :", context)
#         return

#     elapsed = time.time() - start_time

#     if elapsed > threshold:
#         raise ThresholdExceededException(threshold, elapsed)

#     try:
#         data = response.json()
#         print(f"Réponse JSON : nombre de produits récupérés : {len(data['products'])}")
#     except Exception:
#         print("La réponse doit être au format JSON, ici :", response.text)

# Exo 8
def exo8_fetch_with_threshold(url: str, threshold: int):
    print("-----------------------Exo 8------------------------")
    start_time = time.time()
    
    try:
        response = requests.get(url, timeout=threshold)

    except requests.exceptions.Timeout:
        elapsed = time.time() - start_time
        raise ThresholdExceededException(threshold, elapsed)
    
    except Exception as context:
        print("Erreur lors de la requête :", context)
        return

    elapsed = time.time() - start_time
    if elapsed > threshold:
        raise ThresholdExceededException(threshold, elapsed)

    try:
        data = response.json()
        print(f"Réponse JSON : nombre de produits récupérés : {len(data['products'])}")
    except Exception:
        print("La réponse doit être au format JSON, ici :", response.text)

# Exo 9 
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def http_get_exo9(url: str) -> dict:
    print('--------------Exo 9-----------------')
    try :
        r = requests.get(url)
        if r.status_code == 200:
            logging.info(f"Code de retour obtenu : {r.status_code}")
        else:
            logging.critical(f"Erreur HTTP : {r.status_code}")
            raise Exception(f"Erreur HTTP : {r.status_code}")
    except requests.RequestException as exeption:
        logging.critical(f"Erreur lors de la requête HTTP : {exeption}")
        raise
    try : 
        data = r.json()
        logging.info(f"Nombre de retours pour la requête GET : {len(data['products'])}")
    except Exception :
        logging.critical(f"La réponse n'est pas au format JSON mais : {r.text}")
        raise
    return data









if __name__ == "__main__":
    args = parse_command_line_args()

    # Exo 2
    print("------------------------Début EXO 2--------------------------")
    print(f"Protocol : {args.protocol}")
    print(f"Hostname : {args.hostname}")
    print(f"URI : {args.uri}")
    print(f"Threshold : {args.threshold}")
    print("------------------------Fin EXO 2--------------------------")

    # Exo 5 
    data = http_get_V2("https://dummyjson.com/products")
    print(f"Nombre de retour pour la requete get : {len(data['products'])}")
    print("------------------------Fin EXO 5--------------------------")

    # # Exo 7 
    # try:
    #     url = format_url(args.protocol, args.hostname, args.uri)
    #     print(f"URL construite : {url}")
    #     print(f"Seuil : {args.threshold}s")
    #     fetch_with_threshold(url, args.threshold)
    # except ThresholdExceededException as context:
    #     print("Exception levée :", context)
    # except Exception as context:
    #     print("Exo 7 non exécuté :", context)
    
    # Exo 8 
    try:
        url = format_url(args.protocol, args.hostname, args.uri)
        print(f"URL construite : {url}")
        print(f"Seuil : {args.threshold}s")
        exo8_fetch_with_threshold(url, args.threshold)
    except ThresholdExceededException as context:
        print("Exo 8 - Exception levée :", context)

    # Exo 9 
    url = 'https://dummyjson.com/products'
    http_get_exo9(url)

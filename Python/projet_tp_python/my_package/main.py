import requests
import argparse
import sys

# Premier exo :
def http_get() -> dict : 
    r = requests.get('https://dummyjson.com/products')
    print(f"Code de retour obtenu : {r.status_code}")
    if r.status_code != 200: # si le r.status_code est différent de 200 alors on affiche le message d'erreur suivant et le code d'erreur
        raise Exception(f"Erreur HTTP : {r.status_code}")
    return r.json()

data = http_get()
print(f"Nombre de retour pour la requete get : {len(data['products'])}")


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
    print(f"Protocol : {args.protocol}")
    print(f"Hostname : {args.hostname}")
    print(f"URI : {args.uri}")
    print(f"Threshold : {args.threshold}")
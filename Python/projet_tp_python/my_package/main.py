import requests

def http_get() -> object : 
    r = requests.get('https://dummyjson.com/products')
    print(r.status_code)
    if r.status_code != 200:
        raise Exception(f"Erreur HTTP : {r.status_code}")
    return r.json()

data = http_get()
print(data)
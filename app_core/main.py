# Importation de FastAPI, le framework que nous utilisons
from fastapi import FastAPI

# Création d'une instance de l'application FastAPI
# C'est cette instance qui va gérer toutes les requêtes HTTP
app = FastAPI()

# Création d'une première route de test (endpoint HTTP GET sur "/")
@app.get("/")
def read_root():
    """
    Cette fonction est appelée quand quelqu'un accède à l'URL "/".
    Elle retourne un petit message de bienvenue au format JSON.
    """
    return {"message": "Bienvenue sur Ankhoris Core , maitrise la gestion de vos données "}

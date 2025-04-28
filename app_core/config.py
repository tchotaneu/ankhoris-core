# Importation de BaseSettings pour charger automatiquement les variables d'environnement
from pydantic import BaseSettings

# Définition d'une classe Settings pour contenir tous nos paramètres de config
class Settings(BaseSettings):
    # Définir ici les variables d'environnement que l'on veut utiliser
    DB_HOST: str 
    DB_PORT: str 
    DB_USER: str 
    DB_PASSWORD: str 
    DB_NAME: str 

    class Config:
        # Indique qu'on peut aussi charger les variables depuis un fichier ".env" (facultatif)
        env_file = ".env"

# Création d'une instance globale de Settings
# Cela permet d'accéder aux variables partout dans le projet
settings = Settings()

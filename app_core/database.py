# Importation de create_engine pour se connecter à la base
# Importation de sessionmaker pour créer des sessions de base de données
# Importation de declarative_base pour déclarer nos modèles ORM
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Importation de notre fichier de configuration
from app_core.config import settings

# Construction de l'URL de connexion PostgreSQL
DATABASE_URL = f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"

# Création du moteur de base de données SQLAlchemy
# Ce moteur est la "porte" qui parle avec PostgreSQL
engine = create_engine(DATABASE_URL)

# Création de la session locale
# Une session permet d'interagir avec la base (requêtes, insertions, suppressions)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Création de la base de déclaration
# Tous nos futurs modèles ORM hériteront de Base
Base = declarative_base()

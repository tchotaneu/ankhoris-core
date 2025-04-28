# Importation des outils nécessaires de SQLAlchemy
from sqlalchemy import Column, Integer, String, Date
# Importation de la Base pour que notre modèle soit reconnu par SQLAlchemy
from app_core.database import Base

# Définition du modèle Student
class Student(Base):
    """
    Modèle Student : représente un élève dans la base de données.
    Hérite de Base pour être transformé en table PostgreSQL.
    """
    # Définir le nom de la table SQL qui sera créée
    __tablename__ = "students"

    # Colonnes (champs) de la table "students"

    id = Column(Integer, primary_key=True, index=True)
    """
    Identifiant unique de l'élève (clé primaire auto-incrémentée).
    """

    first_name = Column(String, nullable=False)
    """
    Prénom de l'élève (obligatoire).
    """

    last_name = Column(String, nullable=False)
    """
    Nom de famille de l'élève (obligatoire).
    """

    date_of_birth = Column(Date, nullable=True)
    """
    Date de naissance de l'élève (facultatif pour l'instant).
    """

    email = Column(String, unique=True, index=True, nullable=True)
    """
    Adresse email de l'élève (facultatif et unique s'il est renseigné).
    """

    phone = Column(String, nullable=True)
    """
    Numéro de téléphone de l'élève (facultatif).
    """

    class_id = Column(Integer, nullable=True)
    """
    Identifiant de la classe de l'élève (sera relié à la table des classes plus tard).
    """

from pydantic import BaseModel, Field
import json

# Définir le modèle Pydantic pour les adhérents
class Adherent(BaseModel):
    id: int = Field(description="Identifiant unique de l'adhérent")
    profil: dict = Field(description="Informations personnelles de l'adhérent")
    cotisation: dict = Field(description="Informations sur la cotisation de l'adhérent")
    cours_suivis: list = Field(description="Liste des cours suivis par l'adhérent")
    evenements_participes: list = Field(description="Liste des événements auxquels l'adhérent a participé")
    responsables_legaux: dict = Field(description="Informations sur les responsables légaux de l'adhérent")

# Charger les données JSON depuis le fichier
def load_data():
    with open("./data.json", "r") as f:
        data = json.load(f)
    return [Adherent(**adherent) for adherent in data]


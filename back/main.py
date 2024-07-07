from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Adherent, load_data
import json

origins = [
    "http://localhost:5173/test" 
]
# Charger les données JSON depuis le fichier
def load_data():
    with open("./data.json", "r") as f:
        data = json.load(f)
    return [Adherent(**adherent) for adherent in data]


# Créer l'application FastAPI
app = FastAPI()

# Ajouter le middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Autoriser cette origine
    allow_credentials=True,
    allow_methods=["*"],  # Autoriser toutes les méthodes (GET, POST, etc.)
    allow_headers=["*"],  # Autoriser tous les en-têtes
)

@app.get("/")
async def root():
    return {"message": "Hello !"}

# Obtenir la liste de tous les adhérents
@app.get("/adherents")
def get_all_adherents():
    adherents = load_data()
    return adherents

# Obtenir un adhérent spécifique par son ID
@app.get("/adherents/{adherent_id}")
def get_adherent_by_id(adherent_id: int):
    adherents = load_data()
    for adherent in adherents:
        if adherent.id == adherent_id:
            return adherent
    return {"message": "Adhérent introuvable"}
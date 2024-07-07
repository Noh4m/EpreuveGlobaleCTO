# EpreuveGlobaleCTO

## Description

Ce projet est une application web composée d'un front-end développé en Svelte et d'un back-end en Python utilisant Poetry pour la gestion des dépendances.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants sur votre machine :

- Node.js (version 12 ou supérieure)
- npm (version 6 ou supérieure)
- Python (version 3.8 ou supérieure)
- Poetry (version 1.1 ou supérieure)

## Démarrage du Front-end (Svelte)

### Installation

1. Clonez le dépôt du projet :
   ```bash
   git clone https://github.com/Noh4m/EpreuveGlobaleCTO
   cd votre-repo/front-end

## Installation et démarrage du Front-end (Svelte) : 
  ```bash
  cd Front
```

## Installez les dépendances :
  ```bash
  npm install
  npm run dev
   ```
- Ouvrez votre navigateur et accédez à http://localhost:5000](http://localhost:5173. Vous devriez voir votre application Svelte en cours d'exécution.

## Installation et démarrage du Back-end (pyhton, Poetry) :
   - Ouvrez un nouveau terminal puis
  ```bash
  cd back-end
  ```
  - Installez Poetry si ce n'est pas déjà fait 
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```
  - Installez les dépendances
    ```bash
    poetry install
    ```
  - Démarrage du projet back-end
    ```bash
    poetry run uvicorn main:app --reload
    ```
## Obtenir tout les adhérents 
  URL : http://127.0.0.1:8000/adherents
  Méthode : GET
  Description : Cette route retourne les informations de tous les adhérents.

  ## Obtenir un adhérent spécifique par son ID
  URL : http://127.0.0.1:8000/adherents/adherents/{adherent_id}
  Méthode : GET
  Description : Cette route retourne les informations d'un adhérent spécifique en fonction de son ID.

## Envoyer un mail
  Pour commencer il vas falloir configurer votre email dans le fichier config.py et changer l'adresse mail dans : 
  ```bash
  "email": "Votre adresse mail"
  ```
  et il faut aussi mettre votre mot de passe pour pouvoir vous connecter avant l’envoi du mail :
  ```bash
  "pwd": "Votre mot de passe"
  ```
  - Pour envoyer votre mail il suffit de faire la commande :
    ```bash
    python3 sendmail.py
    ```
    Si tout se passe bien vous auriez le message suivant :
    ```bash
    Email sent
    ```
    
  

import os
import requests
from datetime import datetime

# Récupération des secrets depuis l'environnement GitHub Actions
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Liste de tes anecdotes (tu peux en ajouter d'autres ici)
anecdotes = [
    "Anecdote 1 : Les flamants roses dorment souvent sur une seule patte.",
    "Anecdote 2 : Le miel ne périme jamais. On en a retrouvé comestible dans les tombes égyptiennes.",
    "Anecdote 3 : Les bananes sont courbées parce qu'elles poussent vers le soleil en défiant la gravité."
]

def envoyer_anecdote():
    if not TOKEN or not CHAT_ID:
        print("Erreur : Les secrets Telegram ne sont pas configurés.")
        return

    # Sélectionner une anecdote en fonction du jour de l'année
    jour_annee = datetime.now().timetuple().tm_yday
    index = (jour_annee - 1) % len(anecdotes)
    message = anecdotes[index]

    # Envoi via l'API Telegram
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        print("Anecdote envoyée avec succès !")
    else:
        print(f"Erreur d'envoi : {response.text}")

if __name__ == "__main__":
    envoyer_anecdote()

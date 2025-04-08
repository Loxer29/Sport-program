import requests
import os
from datetime import datetime

# Variables d'environnement pour stocker le token et le chat_id de manière sécurisée
TOKEN = os.environ.get('TELEGRAM_TOKEN')
CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')

# Liste des messages détaillés
messages = {

    0: """Lundi 💪 :
• 3 séries de 10 pompes modifiées : En position planche avec les genoux au sol, abaisse ton corps en pliant les coudes, puis repousse pour revenir à la position initiale.
• 30 secondes de planche : Garde une position de planche, corps bien droit, bras tendus et engage tes abdos.
• 15 squats : Place tes pieds à la largeur des épaules, descends les hanches comme si tu t’assoyais sur une chaise, puis remonte.
Durée estimée : 10 min""",
    
    1: """Mardi 🏋️ :
• 3 séries de 12 dips sur chaise : Assis sur une chaise, place les mains à côté des hanches, descends le buste en pliant les coudes et pousse pour revenir.
• 10 fentes avant (chaque jambe) : Fais un grand pas en avant et abaisse les hanches pour former un angle de 90° avec les deux jambes, puis remonte.
• 30 jumping jacks : Saute en écartant les jambes et levant les bras au-dessus de la tête, puis ramène-les vers le centre en sautant.
Durée estimée : 10 min""",

    2: """Mercredi 🧑‍🦯 :
• 3 séries de 8 pompes diamant : En position de planche, place tes mains sous ton torse pour former un diamant avec tes doigts, abaisse ton buste, puis pousse pour revenir.
• 12 squats sumo : Prends une position plus large que les hanches avec les pieds tournés vers l’extérieur, descends en pliant les genoux, puis remonte.
• 45 secondes de planche latérale (chaque côté) : Allonge-toi sur le côté, appuie-toi sur un coude et garde le corps bien droit, sans que les hanches ne touchent le sol.
Durée estimée : 10 min""",

    3: """Jeudi 💪 :
• 2 séries de 12 pompes inclinées : Place tes mains sur une surface surélevée (comme une table ou un banc), abaisse ton buste en pliant les coudes, puis repousse pour revenir.
• 15 extensions de triceps : Avec un poids ou sans, tiens tes bras au-dessus de la tête, plie les coudes pour faire descendre les mains derrière la tête, puis remonte.
• 20 élévations latérales : Tiens des poids légers, lève les bras sur les côtés jusqu’à la hauteur des épaules, puis redescends doucement.
Durée estimée : 10 min""",

    4: """Vendredi 🏋️ :
• 3 séries de 15 squats partiels (focus genoux) : Descends seulement légèrement, en gardant les genoux au-dessus des pieds, sans les laisser dépasser de la ligne des orteils.
• 10 pompes standards : En position planche, abaisse le corps en pliant les coudes, puis repousse pour revenir à la position initiale.
• 30 crunchs : Allongé sur le dos, plie les genoux et contracte les abdos pour soulever les épaules du sol.
Durée estimée : 10 min""",

    5: """Samedi 🚶‍♂️ :
• Étirements (10 min) : Étire tout le corps, en te concentrant sur les jambes, les bras et le dos.
• Marche active recommandée (20-30 min) : Marche à un rythme rapide, en bougeant bien les bras et les jambes.
Durée estimée : 10-30 min""",

    6: """Dimanche 🧘‍♀️ :
• Étirements (10 min) : Prends ton temps pour étirer les principaux groupes musculaires.
• Marche active recommandée (20-30 min) : Garde une bonne posture et reste actif tout au long de la marche.
Durée estimée : 10-30 min"""
}

def send_message():
    # Déterminer le jour de la semaine (0=lundi, 6=dimanche)
    jour = datetime.now().weekday()
    message = messages.get(jour, "Aujourd'hui, reste actif !")

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {'chat_id': CHAT_ID, 'text': message}

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Message envoyé avec succès")
    else:
        print(f"Erreur lors de l'envoi du message: {response.status_code} - {response.text}")

# Exécuter la fonction directement
if __name__ == "__main__":
    send_message()

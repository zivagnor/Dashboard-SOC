import json

alertes=[
    {"niveau":"Connexion suspecte", "ip": "192.168.1.105", "niveau": "critique"},
    {"niveau":"Accès non autorisé", "ip": "192.168.1.106", "niveau": "moyen"},
    {"niveau":"Tentative de brute force", "ip": "192.168.1.107", "niveau": "élevé"},
    {"niveau":"Activité anormale", "ip": "192.168.1.108", "niveau": "faible"},
    {"niveau":"Fuite de données", "ip": "192.168.1.109", "niveau": "critique"},
    {"niveau":"Malware détecté", "ip": "192.168.1.110", "niveau": "élevé"}
]


nc=0
ne=0
nm=0
n=0

for alerte in alertes:
    if alerte["niveau"] == "critique":
        print(alerte)
        nc+=1
    elif alerte["niveau"] == "élevé":
        print(alerte)
        ne+=1
    elif alerte["niveau"] == "moyen":
        print(alerte)
        nm+=1
    else:
        print(alerte)
        n+=1

print(f"Niveau critique: ", nc, "   Niveau élevé: ",ne, "   Niveau moyen: ", nm, "   Niveau faible ou inconnu: ", n)

with open("data/alertes.json", "w", encoding="utf-8") as fichier:
    json.dump(alertes, fichier, ensure_ascii=False, indent=2)
print("On est le combien ? (Écris seulement le nombre)")
jour = int(input())
print("Il est quelle heure ? (Écris seulement le nombre)")
heure = int(input())
print("Combien de minutes se sont écoulées ?(Écris seulement le nombre)")
minute = int(input())

Vjour = jour - 1
res1 = (Vjour*24) * 60
res2 = heure*60
res3 = minute

ResultatF = res1 + res2 + res3
print(f"Depuis le début du mois,{ResultatF} minutes se sont écoulées.")


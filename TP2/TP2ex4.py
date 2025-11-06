BASE = 4
fromage = 800.0
eau = 2.0
ail = 2.0
pain = 400.0
nbConvives = int(input("Entrez le nombre de personne(s) conviées à la fondue : "))
fromage = fromage * nbConvives / BASE
eau = eau * nbConvives / BASE
ail = ail * nbConvives / BASE
pain = pain * nbConvives / BASE

print(f"\nPour faire une fondue fribourgeoise pour {nbConvives} personne(s), il vous faut :")
print(f"- {fromage:.1f} gr de fromage")
print(f"- {eau:.1f} dl d'eau")
print(f"- {ail:.1f} gousse(s) d'ail")
print(f"- {pain:.1f} gr de pain")

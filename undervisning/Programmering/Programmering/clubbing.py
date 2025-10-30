def go_to_club(navn, alder):
    if alder < 18: 
        resultat = f"Yo, du {navn}, du er for ung!"
    else: 
        resultat = f"Hei, {navn}, its time to party!"

    return resultat + "!"

print(go_to_club("Ola", 22))

def go_to_club (navn, alder):
    if alder < 18:
        return f"Yo {navn}, du er for ung!"
    
    result = f"Hei, {navn}! Its time to party"
    return result + "!"

print(go_to_club("Luwei", 26))

def cubed(num):
    return num ** 3

cubed(2)
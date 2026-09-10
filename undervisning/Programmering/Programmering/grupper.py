import random
from pathlib import Path

elever = [
    "Anna", "Jonas", "Emil", "Mia", "Sofie", "Oskar", "Ella", "Noah",
    "Hanna", "Liam", "Amalie", "Tobias", "Thea", "Oliver", "Leah", "Aksel",
    "Ingrid", "Elias", "Sara", "Henrik"
]

# konfigurer gruppestørrelse
gruppestorrelse = 4

# stokker listen og deler i grupper
random.shuffle(elever)
grupper = [elever[i:i + gruppestorrelse] for i in range(0, len(elever), gruppestorrelse)]

# lag HTML-innhold
html_start = """<!DOCTYPE html>
<html lang="no">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Grupper</title>
<style>
  body { font-family: Arial, sans-serif; background:#f7f7fb; margin:20px; }
  .container { display:flex; flex-wrap:wrap; gap:16px; justify-content:flex-start; }
  .card {
    background: white;
    border: 2px solid #e0e0ee;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.04);
    padding: 14px;
    width: 220px;
  }
  .card h3 { margin: 0 0 8px 0; color:#26325b; font-size:18px; }
  .card ul { padding-left: 18px; margin: 0; }
  .card li { margin:6px 0; color:#333; }
  .note { margin-top: 18px; color:#666; font-size:14px; }
</style>
</head>
<body>
<h1>Tilfeldige grupper (gruppestørrelse = {size})</h1>
<div class="container">
""".format(size=gruppestorrelse)

html_cards = ""
for i, gruppe in enumerate(grupper, start=1):
    # hvis siste gruppe er mindre enn gruppestørrelse, vis det (f.eks. 2 personer)
    html_cards += f'  <div class="card">\n'
    html_cards += f'    <h3>Gruppe {i}</h3>\n'
    html_cards += '    <ul>\n'
    for elev in gruppe:
        html_cards += f'      <li>{elev}</li>\n'
    html_cards += '    </ul>\n'
    html_cards += '  </div>\n'

html_end = """</div>
<p class="note">Obs: Hvis antall elever ikke går opp i {size}, vil siste gruppe ha færre enn {size} elever.</p>
</body>
</html>
""".format(size=gruppestorrelse)

html = html_start + html_cards + html_end

# skriv til fil
out = Path("grupper.html")
out.write_text(html, encoding="utf-8")
print(f"Ferdig — filen '{out}' er laget. Åpne den i nettleseren for å se gruppene.")

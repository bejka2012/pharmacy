import pandas as pd
import random

# Nastavení semene pro reprodukovatelnost
random.seed(42)

# Seznam lékárenských produktů
produkty = [
    "Paralen", "Ibalgin", "Stoptusin", "Levopront", "Calcium",
    "Aspirin", "Panadol", "Nurofen", "Coldrex", "Theraflu",
    "ACC Long", "Ambrobene", "Mucosolvan", "Hedelix", "Prospan",
    "Olynth", "Nasivin", "Sanorin", "Septolete", "Strepsils",
    "Neo-angin", "Tantum Verde", "Orofar", "Magne B6", "Celaskon",
    "Vitamin D", "B-komplex", "Zodac", "Zyrtec", "Claritin"
]

vyrobci = ["Zentiva", "Teva", "Sandoz", "Krka", "Pfizer", "Bayer", "Sanofi", "GSK", "Roche", "Novartis"]

kategorie = ["Analgetika", "Antitusika", "Antipyretika", "Antihistaminika", "Vitamíny", "Dekongestiva", "Mukolytika", "Antiseptika"]
segmenty = ["Bolest", "Kašel", "Horečka", "Alergie", "Dýchací cesty", "Vitamíny", "Imunita", "Nosní obtíže"]

# Generování 1000 unikátních produktů
data_dim_zbozi = []
for i in range(1, 1001):
    produkt = random.choice(produkty) + f" {random.randint(100, 999)}mg"
    vyrobce = random.choice(vyrobci)
    sukl_cislo = f"{random.randint(100000, 999999)}.{random.randint(10, 99)}"
    kategorie_vyrobku = random.choice(kategorie)
    segment_vyrobku = random.choice(segmenty)
    data_dim_zbozi.append([i, produkt, vyrobce, sukl_cislo, kategorie_vyrobku, segment_vyrobku])

# Vytvoření DataFrame
df_dim_zbozi = pd.DataFrame(data_dim_zbozi, columns=["ID_zbozi", "Nazev", "Vyrobce", "SUKL_cislo", "Kategorie", "Segment"])

# Uložení DataFrame do Excel souboru
excel_filename = "dim_zbozi.xlsx"
df_dim_zbozi.to_excel(excel_filename, index=False)

print(f"Data byla úspěšně uložena do souboru: {excel_filename}")

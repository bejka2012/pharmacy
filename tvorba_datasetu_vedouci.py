import pandas as pd
import random
from datetime import datetime, timedelta

# Pro reprodukovatelnost výsledků
random.seed(42)

# Funkce pro generování náhodné adresy
def generate_address():
    streets = [
        "Náměstí Svobody", "Hlavní třída", "Masarykova", "Smetanovo náměstí",
        "Sokolovská", "Květná", "Dlouhá", "Krátká", "Javorová"
    ]
    street = random.choice(streets)
    number = random.randint(1, 100)
    return f"{street} {number}"

# Funkce pro generování náhodného data ve formátu YYYY-MM-DD
def generate_random_date(start_date_str, end_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime("%Y-%m-%d")

# Seznamy jmen
# Pro muže: explicitně zahrnujeme Ondřej a Vladimír, zbytek vybereme z dalších
male_names = ["Ondřej", "Vladimír"]
additional_male_names = ["Jan", "Petr", "Martin", "Josef", "Marek", "Lukáš", "Michal", "Tomáš"]
# Vybereme 13 náhodných jmen z additional_male_names (s opakováním povolujeme) pro doplnění celkového počtu 15
male_names += random.choices(additional_male_names, k=13)
random.shuffle(male_names)  # promícháme pořadí

# Pro ženy použijeme 15 unikátních jmen
female_names = ["Eva", "Anna", "Jana", "Martina", "Lucie", "Veronika", "Petra", "Karla", "Alena", "Lenka", "Helena", "Barbora", "Michaela", "Dagmar", "Věra"]

# Seznam příjmení (budou společná pro muže i ženy)
surnames = [
    "Novák", "Svoboda", "Dvořák", "Černý", "Procházka", "Kučera", "Veselý", 
    "Horák", "Němec", "Pokorný", "Pospíšil", "Král", "Urban", "Kolář", "Kříž", "Málek"
]

data_dim_vedouci = []

# Generování 15 mužských záznamů
for jmeno in male_names:
    prijmeni = random.choice(surnames)
    adresa = generate_address()
    # Datum narození mezi 1960-01-01 a 1990-12-31
    datum_narozeni = generate_random_date("1960-01-01", "1990-12-31")
    # Datum nástupu mezi 2005-01-01 a 2020-12-31
    datum_nastupu = generate_random_date("2005-01-01", "2020-12-31")
    data_dim_vedouci.append([jmeno, prijmeni, adresa, datum_narozeni, datum_nastupu])

# Generování 15 ženských záznamů
for jmeno in female_names:
    prijmeni = random.choice(surnames)
    adresa = generate_address()
    datum_narozeni = generate_random_date("1960-01-01", "1990-12-31")
    datum_nastupu = generate_random_date("2005-01-01", "2020-12-31")
    data_dim_vedouci.append([jmeno, prijmeni, adresa, datum_narozeni, datum_nastupu])

# Vytvoření DataFrame a přiřazení primárního klíče ID_vedouci
df_dim_vedouci = pd.DataFrame(data_dim_vedouci, columns=["jmeno", "prijmeni", "adresa", "datum_narozeni", "datum_nastupu"])
df_dim_vedouci.insert(0, "ID_vedouci", range(1, len(df_dim_vedouci) + 1))

# Uložení do Excel souboru
excel_filename = "dim_vedouci.xlsx"
df_dim_vedouci.to_excel(excel_filename, index=False)

print(f"Data byla úspěšně uložena do souboru: {excel_filename}")

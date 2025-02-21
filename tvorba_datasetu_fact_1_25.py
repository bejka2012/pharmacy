import pandas as pd
import random
from datetime import datetime, timedelta

# Pro reprodukovatelnost výsledků
random.seed(42)

# Počet řádků ve faktovce
num_rows = 5000

data_fact = []

# Definice období ledna 2025
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 1, 31)
days_range = (end_date - start_date).days

for _ in range(num_rows):
    # Cizí klíče: ID_zbozi, ID_lekarna, ID_vedouci
    id_zbozi = random.randint(1, 1000)
    id_lekarna = random.randint(1, 30)
    id_vedouci = random.randint(1, 30)
    
    # Náhodné datum v lednu 2025
    random_day = random.randint(0, days_range)
    date = start_date + timedelta(days=random_day)
    date_str = date.strftime("%Y-%m-%d")
    
    # Metodické údaje
    pocet_prodanych_ks = random.randint(1, 20)
    
    # Ceny bez desetinných míst: použití náhodné hodnoty jako celé číslo
    nakupni_cena = random.randint(20, 500)
    
    # Prodejní cena = nákupní cena * markup (markup mezi 1.05 a 1.50) - výsledek zaokrouhlen na celé číslo
    markup = random.uniform(1.05, 1.50)
    prodejni_cena = int(round(nakupni_cena * markup, 0))
    
    # Marže = (prodejní cena - nákupní cena) * počet prodaných ks
    marze = (prodejni_cena - nakupni_cena) * pocet_prodanych_ks
    
    data_fact.append([
        id_zbozi,
        id_lekarna,
        id_vedouci,
        date_str,
        pocet_prodanych_ks,
        nakupni_cena,
        prodejni_cena,
        marze
    ])

# Vytvoření DataFrame pro faktovku
df_fact = pd.DataFrame(
    data_fact,
    columns=[
        "ID_zbozi",
        "ID_lekarna",
        "ID_vedouci",
        "datum",
        "pocet_prodanych_ks",
        "nakupni_cena_CZK",
        "prodejni_cena_CZK",
        "marze_CZK"
    ]
)

# Uložení DataFrame do Excel souboru s názvem fact_prodej_jan.xlsx
excel_filename = "fact_prodej_jan.xlsx"
df_fact.to_excel(excel_filename, index=False)

print(f"Data byla úspěšně uložena do souboru: {excel_filename}")

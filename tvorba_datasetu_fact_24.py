import pandas as pd
import random
from datetime import datetime, timedelta

# Pro reprodukovatelnost výsledků
random.seed(42)

# Počet řádků ve faktové tabulce
num_rows = 5000
data_fact = []

# Definice období pro celý rok 2024
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
days_range = (end_date - start_date).days

for _ in range(num_rows):
    # Cizí klíče: produkty, lékárny, vedoucí
    id_zbozi = random.randint(1, 1000)
    id_lekarna = random.randint(1, 30)
    id_vedouci = random.randint(1, 30)
    
    # Náhodné datum v roce 2024
    random_day = random.randint(0, days_range)
    date = start_date + timedelta(days=random_day)
    date_str = date.strftime("%Y-%m-%d")
    
    # Metodické údaje
    pocet_prodanych_ks = random.randint(1, 20)
    nakupni_cena = random.randint(20, 500)
    markup = random.uniform(1.05, 1.50)
    prodejni_cena = int(round(nakupni_cena * markup, 0))
    
    # Marže: rozdíl mezi prodejní a nákupní cenou
    marze = prodejni_cena - nakupni_cena
    
    # Tržba: počet prodaných ks * marže
    trzba = pocet_prodanych_ks * marze
    
    data_fact.append([
        id_zbozi,
        id_lekarna,
        id_vedouci,
        date_str,
        pocet_prodanych_ks,
        nakupni_cena,
        prodejni_cena,
        marze,
        trzba
    ])

# Vytvoření DataFrame pro faktovou tabulku
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
        "marze_CZK",
        "trzba_CZK"
    ]
)

# Uložení DataFrame do CSV souboru
csv_filename = "fact_prodej_2024.csv"
df_fact.to_csv(csv_filename, index=False)

print(f"Data byla úspěšně uložena do souboru: {csv_filename}")


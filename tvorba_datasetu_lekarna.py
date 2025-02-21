import pandas as pd
import random

# Pro reprodukovatelnost výsledků
random.seed(42)

# Seznam dalších větších měst v ČR
other_cities = [
    "Plzeň", "Liberec", "Olomouc", "Hradec Králové", "Pardubice",
    "Zlín", "České Budějovice", "Ústí nad Labem", "Jihlava", 
    "Mladá Boleslav", "Karlovy Vary", "Teplice", "Děčín"
]

# Funkce pro generování náhodné adresy
def generate_address():
    streets = [
        "Náměstí Svobody", "Hlavní třída", "Masarykova", "Smetanovo náměstí",
        "Sokolovská", "Květná", "Dlouhá", "Krátká", "Javorová"
    ]
    street = random.choice(streets)
    number = random.randint(1, 100)
    return f"{street} {number}"

data_dim_lekarna = []

# Přidání 3 poboček pro Prahu
for _ in range(3):
    data_dim_lekarna.append(["Praha", generate_address()])

# Přidání 3 poboček pro Brno
for _ in range(3):
    data_dim_lekarna.append(["Brno", generate_address()])

# Přidání 3 poboček pro Ostravu
for _ in range(3):
    data_dim_lekarna.append(["Ostrava", generate_address()])

# Pro zbylých 21 řádků vybereme náhodně město z other_cities
for _ in range(21):
    city = random.choice(other_cities)
    data_dim_lekarna.append([city, generate_address()])

# Vytvoření DataFrame a přidání primárního klíče ID_lekarna
df_dim_lekarna = pd.DataFrame(data_dim_lekarna, columns=["mesto", "adresa"])
df_dim_lekarna.insert(0, "ID_lekarna", range(1, len(df_dim_lekarna) + 1))

# Vytvoření sloupce nazev_lekarny:
# Pokud je v daném městě více záznamů, přidá se pořadové číslo, jinak se ponechá jen název města.
df_dim_lekarna["city_count"] = df_dim_lekarna.groupby("mesto")["mesto"].transform("size")
df_dim_lekarna["order"] = df_dim_lekarna.groupby("mesto").cumcount() + 1

df_dim_lekarna["nazev_lekarny"] = df_dim_lekarna.apply(
    lambda row: f"{row['mesto']} {row['order']}" if row["city_count"] > 1 else row["mesto"],
    axis=1
)

# Odstranění pomocných sloupců
df_dim_lekarna.drop(columns=["city_count", "order"], inplace=True)

# Uložení DataFrame do Excel souboru
excel_filename = "dim_lekarna.xlsx"
df_dim_lekarna.to_excel(excel_filename, index=False)

print(f"Data byla úspěšně uložena do souboru: {excel_filename}")

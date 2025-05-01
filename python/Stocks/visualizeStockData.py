import pandas as pd
import matplotlib.pyplot as plt

# CSV-Datei einlesen
df = pd.read_csv("StockInputData.csv", parse_dates=["Date"])

# Spalte "Change" bereinigen und umwandeln
df["Change"] = df["Change"].str.replace('%', '').str.replace(',', '.').astype(float)

# Daten sortieren
df.sort_values(by="Date", inplace=True)

# Liste der Unternehmen
companies = df["Company"].unique()
num_companies = len(companies)

# Große Figure mit 2 Zeilen pro Unternehmen (1: Preis, 2: Veränderung)
fig, axes = plt.subplots(num_companies, 2, figsize=(16, 4 * num_companies), sharex='col')

# Falls nur 1 Unternehmen (damit axes immer 2D bleibt)
if num_companies == 1:
    axes = [axes]

for i, company in enumerate(companies):
    company_data = df[df["Company"] == company]

    # Preisverlauf (linke Spalte)
    ax_price = axes[i][0]
    ax_price.plot(company_data["Date"], company_data["Price"], color="blue")
    ax_price.set_title(f"{company} – Preisverlauf")
    ax_price.set_ylabel("Preis (€)")
    ax_price.grid(True)

    # Veränderung (rechte Spalte)
    ax_change = axes[i][1]
    ax_change.bar(company_data["Date"], company_data["Change"], color="orange")
    ax_change.axhline(0, color="gray", linestyle="--", linewidth=1)
    ax_change.set_title(f"{company} – Veränderung (%)")
    ax_change.set_ylabel("Veränderung (%)")
    ax_change.grid(True)

# Gemeinsame X-Achse
plt.xlabel("Datum")

# Layout anpassen
plt.tight_layout()

# Bild speichern
plt.savefig("alle_aktienverläufe.png", dpi=300)

# Auch anzeigen
plt.show()

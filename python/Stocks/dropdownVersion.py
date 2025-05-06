import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

from CleanPrice import clean_price

# CSV-Datei einlesen
df = pd.read_csv("StockInputData.csv", parse_dates=["Date"])

# "Change" Spalte bereinigen
df["Change"] = pd.to_numeric(
    df["Change"].str.replace('%', '', regex=False).str.replace(',', '.', regex=False),
    errors='coerce'
)

# Daten sortieren
df.sort_values(by="Date", inplace=True)

# Daten vorbereiten- Preise umformatieren
df["Price"] = df["Price"].apply(clean_price)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# Unternehmen extrahieren
companies = df["Company"].unique()

# Subplots vorbereiten: 2 Zeilen (Price oben, Change unten), 1 Spalte
fig = make_subplots(
    rows=2, cols=1,
    shared_xaxes=True,
    subplot_titles=("Preisverlauf (€)", "Tägliche Veränderung (%)")
)

# Traces für jedes Unternehmen vorbereiten
dropdown_buttons = []
for company in companies:
    company_data = df[df["Company"] == company].sort_values(by="Date")

    # Preis (Linienplot)
    price_trace = go.Scatter(
        x=company_data["Date"],
        y=company_data["Price"],
        name=f"{company} Preis",
        visible=False
    )

    # Veränderung (Balken)
    change_trace = go.Bar(
        x=company_data["Date"],
        y=company_data["Change"],
        name=f"{company} Veränderung",
        marker_color="orange",
        visible=False
    )

    # Traces zum Plot hinzufügen
    fig.add_trace(price_trace, row=1, col=1)
    fig.add_trace(change_trace, row=2, col=1)

    # Button konfigurieren
    visibility = [False] * (2 * len(companies))
    idx = list(companies).index(company)
    visibility[2 * idx] = True     # Preis
    visibility[2 * idx + 1] = True # Veränderung

    dropdown_buttons.append({
        "label": company,
        "method": "update",
        "args": [{"visible": visibility},
                 {"title": f"{company} – Interaktive Aktienanalyse"}]
    })

# Erste Firma standardmäßig sichtbar machen
fig.data[0].visible = True
fig.data[1].visible = True

# Layout aktualisieren
fig.update_layout(
    updatemenus=[{
        "buttons": dropdown_buttons,
        "direction": "down",
        "showactive": True,
        "x": 0.0,
        "xanchor": "left",
        "y": 1.15,
        "yanchor": "top"
    }],
    height=700,
    title=f"{companies[0]} – Interaktive Aktienanalyse",
    xaxis_title="Datum",
    yaxis_title="Preis (€)",
    xaxis2_title="Datum",
    yaxis2_title="Veränderung (%)",
    template="plotly_white"
)

# Interaktives Plot anzeigen
fig.show()
"""Dash dashboard starter. Uses a local CSV if available."""
from pathlib import Path
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

DATA = Path("data/cleaned_launches.csv")
if DATA.exists():
    df = pd.read_csv(DATA)
else:
    # Empty, clearly labelled fallback: replace with cleaned course dataset.
    df = pd.DataFrame(columns=["launch_site", "landing_success", "launch_year", "payload_mass_kg"])

app = Dash(__name__)
sites = sorted(df["launch_site"].dropna().astype(str).unique()) if not df.empty else []
site_options = [{"label": "All sites", "value": "ALL"}] + [{"label": s, "value": s} for s in sites]

app.layout = html.Div([
    html.H1("SpaceX Falcon 9 Landing Analysis"),
    html.P("Load data/cleaned_launches.csv to populate the dashboard."),
    html.Label("Launch site"),
    dcc.Dropdown(id="site-filter", options=site_options, value="ALL", clearable=False),
    dcc.Graph(id="launch-count-chart"),
    dcc.Graph(id="outcome-chart"),
], style={"maxWidth": "1100px", "margin": "auto", "fontFamily": "Arial"})

@app.callback(
    Output("launch-count-chart", "figure"),
    Output("outcome-chart", "figure"),
    Input("site-filter", "value")
)
def update_charts(site):
    filtered = df.copy()
    if not filtered.empty and site != "ALL":
        filtered = filtered[filtered["launch_site"].astype(str) == site]
    if filtered.empty:
        empty = px.scatter(title="No data loaded — add cleaned_launches.csv")
        return empty, px.scatter(title="No data loaded — add cleaned_launches.csv")
    if "launch_year" in filtered.columns:
        trend = filtered.groupby("launch_year", dropna=True).size().reset_index(name="launch_count")
        fig1 = px.bar(trend, x="launch_year", y="launch_count", title="Launches by year")
    else:
        fig1 = px.bar(title="launch_year column required")
    if {"launch_site", "landing_success"}.issubset(filtered.columns):
        counts = filtered.groupby(["launch_site", "landing_success"]).size().reset_index(name="count")
        fig2 = px.bar(counts, x="launch_site", y="count", color="landing_success",
                      barmode="group", title="Landing outcomes by launch site")
    else:
        fig2 = px.bar(title="launch_site and landing_success columns required")
    return fig1, fig2

if __name__ == "__main__":
    app.run(debug=True)

# app.py
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
from scraper import scrape_jobs_df

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout
app.layout = dbc.Container([
    html.H1("Indeed Job Dashboard", className="my-4 text-center"),

    dbc.Row([
        dbc.Col(dcc.Input(id="job-input", type="text", value="developer", placeholder="Job title", className="form-control")),
        dbc.Col(dcc.Input(id="city-input", type="text", value="London", placeholder="City", className="form-control")),
        dbc.Col(html.Button("Search", id="search-btn", className="btn btn-primary"))
    ], className="mb-4"),

    dbc.Row(id="job-output", className="g-3")  # g-3 adds spacing between cards
], fluid=True)


@app.callback(
    Output("job-output", "children"),
    Input("search-btn", "n_clicks"),
    [Input("job-input", "value"), Input("city-input", "value")]
)
def update_jobs(n_clicks, job, city):
    if not n_clicks:
        return html.P("Enter a job and city, then click Search.", className="text-muted")
    
    jobs_df = scrape_jobs_df(job, city, limit=20)

    if jobs_df.empty:
        return html.P("No jobs found.", className="text-danger")
    
    # Create a card for each job
    cards = []
    for _, row in jobs_df.iterrows():
        cards.append(
            dbc.Col(
                dbc.Card(
                    dbc.CardBody([
                        html.H5(row['title'], className="card-title"),
                        html.P(f"{row['company']}", className="card-subtitle"),
                        html.P(f"{row['location']}", className="card-text"),
                    ])
                ),
                width=4  # 3 cards per row
            )
        )
    
    return cards


if __name__ == "__main__":
    app.run(debug=True)

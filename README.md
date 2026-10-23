# SpaceX Falcon 9 First-Stage Landing Prediction

This repository package provides a reproducible workflow for the IBM Applied Data Science Capstone.

## Important before submission
- Add your own public GitHub repository URL to the PDF and submission form.
- Run the notebooks from top to bottom in an environment with internet access.
- Review the data source and target definition carefully. Do not report metrics until the executed notebook produces them.
- Save chart images, the Folium HTML map, dashboard screenshots, and model outputs under `outputs/`.
- This package does not claim that its scripts have been run in your Coursera environment.

## Contents
- `notebooks/01_data_collection_and_eda.ipynb`: API retrieval, data checks, EDA and charts.
- `notebooks/02_sql_analysis.ipynb`: SQLite table setup and example queries.
- `notebooks/03_folium_map.ipynb`: interactive launch-site map starter.
- `notebooks/04_predictive_analysis.ipynb`: target definition, preprocessing, train/test evaluation.
- `src/dashboard_app.py`: Plotly Dash dashboard starter.
- `src/collect_data.py`: API collection script.
- `sql/spacex_analysis.sql`: SQL queries.
- `requirements.txt`: Python dependencies.

## Data source
SpaceX API v4: https://api.spacexdata.com/v4/launches/past  
API repository: https://github.com/r-spacex/SpaceX-API

The API schema and historical data may change. For graded work, prefer the exact course-provided dataset when the course instructions require it. Keep a copy of the source data and note the retrieval date.

## Setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## Run order
1. Run `src/collect_data.py` or execute notebook 01.
2. Inspect the dataset schema and identify the correct landing outcome fields.
3. Run EDA and save actual charts.
4. Run notebook 02 for SQL outputs.
5. Run notebook 03 to create `outputs/spacex_launch_sites_map.html`.
6. Run notebook 04 after confirming target construction and excluding post-outcome leakage.
7. Run `python src/dashboard_app.py` to open the dashboard locally.

## Evidence required for submission
- A real public GitHub URL containing the completed notebooks and Python files.
- Executed notebooks with outputs visible.
- Actual EDA chart exports and SQL query result screenshots.
- Rendered Folium map and dashboard screenshots.
- Test accuracy, precision, recall, F1-score, and confusion matrix from the executed model.
- Final PDF presentation/report containing evidence-based conclusions.

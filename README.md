# India Education Policy Explorer

## Project Overview

This project explores pupil–teacher ratios (PTR) across Indian states and union territories using publicly available education data. It combines SQL-based analysis, Python data processing, and an interactive Streamlit dashboard to support descriptive comparisons of education indicators.

## Objectives

- Examine pupil–teacher ratios across available school levels.
- Compare reported indicators across states and union territories.
- Calculate descriptive statistics using SQL.
- Inspect missing data and validate dataset quality.
- Present the analysis through an interactive dashboard.

## Technology Stack

- Python
- pandas
- SQL
- SQLite
- Streamlit
- Plotly
- Git and GitHub

## Data Source

UDISE+ 2023–24 pupil–teacher ratio dataset, accessed through India's Open Government Data platform.

Source: https://www.data.gov.in/resource/stateuts-wise-pupil-teacher-ratio-ptr-level-school-education-during-2023-24

## Project Structure

- `app.py` — Streamlit dashboard
- `database_utils.py` — Database connection and SQL execution functions
- `database/` — SQLite database
- `data/` — Raw and processed datasets
- `queries/` — SQL analysis files
- `test_db.py` — Database connection checks
- `test_queries.py` — SQL query execution checks
- `requirements.txt` — Python dependencies

## Methodology

1. Inspect the original public dataset.
2. Clean and validate the data using Python and pandas.
3. Store the processed data in SQLite.
4. Execute SQL queries for descriptive analysis.
5. Visualize results through Streamlit and Plotly.
6. Test database connectivity and query outputs.

## Key Findings

Add verified findings here after executing the analysis. Report the period, units, number of records, and relevant limitations. Do not insert unverified statistics.

## Limitations

Pupil–teacher ratio is a descriptive indicator. It does not independently measure teaching quality, learning outcomes, school resources, or the causal effects of education policies. Missing values and differences in data definitions may affect comparisons.

## Run Locally

1. Install Python.
2. Clone or download this repository.
3. Create and activate a virtual environment.
4. Install dependencies using `pip install -r requirements.txt`.
5. Ensure the SQLite database is available, or build it using the documented data-preparation process.
6. Run `python test_db.py` and `python test_queries.py`.
7. Launch the dashboard using `streamlit run app.py`.

## Future Improvements

- Add further education indicators from reliable sources.
- Improve automated data validation.
- Add reproducible database-building scripts.
- Deploy the dashboard and document the live link.

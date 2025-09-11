# src/import_data.py
from pathlib import Path
import pandas as pd

# project root = the folder above /src
# Building path relative to script
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = PROJECT_ROOT / "data" / "archive" / "co2_emissions_kt_by_country.csv"

def load_data(path: Path | str = DATA_FILE) -> pd.DataFrame:
    return pd.read_csv(path)

def get_US_data():
    # There are no missing vales as determined in 'data_analysis,ipynb'
    df = load_data()

    # Get US data
    US_data = df.loc[df['country_name'] == "United States"]

    # Remove redundant column(s)
    US_data = US_data.drop(['country_code', 'country_name'], axis=1)

    return US_data
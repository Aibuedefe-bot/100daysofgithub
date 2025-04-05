# Create a data validation pipeline using Great Expectations.
import great_expectations as gx

import pandas as pd

dataset = pd.read_csv (
    "korean-dramas-dataset-eda\kdrama_DATASET.csv"
)


# This entrypoint file to be used in development. Start by reading README.md
import demographic_data_analyzer
import pandas as pd
import numpy as np
from unittest import main

# Read the data from csv
df = pd.read_csv("adult.data.csv")

# Test your function by calling it here
demographic_data_analyzer.calculate_demographic_data(df)

# Run unit tests automatically
main(module="test_module", exit=False)

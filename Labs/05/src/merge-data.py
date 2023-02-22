# import libraries
import argparse
import glob
from pathlib import Path
import pandas as pd
import mlflow

# get parameters
parser = argparse.ArgumentParser()
parser.add_argument("--airlines", type=str, help='Path to airlines data')
parser.add_argument("--airports", type=str, help='Path to airports data')
parser.add_argument("--carriers", type=str, help='Path to carriers data')
parser.add_argument('--output_data', type=str, help='Path of output data')
args = parser.parse_args()

df_airlines = pd.read_csv(args.airlines)
df_airports = pd.read_csv(args.airports)
df_carriers = pd.read_csv(args.carriers)

# log processed columns
column_count = (len(df.columns))
mlflow.log_metric('column count output data', column_count)

# set the processed data as output
output_df = df.to_csv((args.output_data) / "output_data.csv")

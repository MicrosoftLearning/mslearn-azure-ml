# import libraries
import argparse
import glob
from pathlib import Path
import pandas as pd
import mlflow

# get parameters
parser = argparse.ArgumentParser()
parser.add_argument("--input_data", type=str, help='Path to input data')
parser.add_argument('--output_data', type=str, help='Path of output data')
args = parser.parse_args()

# load the data (passed as an input dataset)
data_path = args.input_data
all_files = glob.glob(data_path + "/*.csv")
df = pd.concat((pd.read_csv(f) for f in all_files), sort=False)
    
# log row count input data
row_count = (len(df))
mlflow.log_metric('row count input data', row_count)

# remove nulls
df = df.dropna()

# log processed rows
row_count_processed = (len(df))
mlflow.log_metric('row count output data', row_count_processed)

# set the processed data as output
output_df = df.to_csv((Path(args.output_data) / "output_data.csv"))
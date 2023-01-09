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

# set the columns and their datatypes for conversion and parsing
cols = ['Flight_Number_Reporting_Airline', 'Year', 'Quarter', 'Month', 'DayOfWeek', 'DOT_ID_Reporting_Airline', 'OriginCityMarketID',  'DestCityMarketID', 'DepTime', 'DepDelay', 'DepDel15', 'ArrTime', 'ArrDelay', 'ArrDel15', 'CRSDepTime', 'CRSArrTime', 'AirTime', 'Distance', 'Reporting_Airline', 'IATA_CODE_Reporting_Airline', 'Origin', 'OriginCityName', 'Dest', 'DestCityName', 'Cancelled']

dtypes = {'Flight_Number_Reporting_Airline': 'float32', 'Year': 'float32', 'Quarter': 'float32', 'Month': 'float32', 'DayOfWeek': 'float32', 'DOT_ID_Reporting_Airline': 'float32', 'OriginCityMarketID': 'float32', 'DestCityMarketID': 'float32', 'DepTime': 'float32', 'DepDelay': 'float32', 'DepDel15': 'int', 'ArrTime': 'float32', 'ArrDelay': 'float32', 'ArrDel15': 'int', 'CRSDepTime': 'float32', 'CRSArrTime': 'float32', 'AirTime': 'float32', 'Distance': 'float32', 'Reporting_Airline': 'str', 'IATA_CODE_Reporting_Airline': 'str', 'Origin': 'str', 'OriginCityName': 'str', 'Dest': 'str', 'DestCityName': 'str', 'Cancelled': 'str'}

df = pd.read_csv((args.input_data), cols=cols, dtypes=dtypes)[cols]

# log processed columns
column_count = (len(df.columns))
mlflow.log_metric('column count output data', column_count)

# set the processed data as output
output_df = df.to_csv((args.output_data) / "output_data.csv")

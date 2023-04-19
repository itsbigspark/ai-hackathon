"""Simple function offering pre-processing on Titanic data"""

# TODO: Add column list accounting for types

import pandas as pd
import pathlib
import os
from tabulate import tabulate


def pre_process_df(csv_path):
    rec_gender = lambda x: {"male": 0, "female": 1}.get(x)
    rec_embarked = lambda x: {"C": 0, "Q": 1, "S": 2}.get(x)
    with open(csv_path) as csv_file:
        df = pd.read_csv(
            filepath_or_buffer=csv_file,
            header=0,
            converters={"Sex": rec_gender, "Embarked": rec_embarked},
            dtype={"Survived": "bool"},
        )
    return df


#
SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "raw/")

print("Data path: " + DATA_PATH)
print("Train data:")
df_train = pre_process_df(csv_path=os.path.join(DATA_PATH + "train.csv"))
print(tabulate(df_train.head(), tablefmt="psql", showindex=True))
print(df_train.dtypes)
print("Test data:")
df_test = pre_process_df(csv_path=os.path.join(DATA_PATH + "test.csv"))
print(tabulate(df_test.head(), tablefmt="psql", showindex=True))

"""Simple function offering pre-processing on Titanic data"""

# TODO: Add column list accounting for types

import pandas as pd
import pathlib
import os
from tabulate import tabulate
from typing import Final


def pre_process_df(csv_path):
    rec_gender = lambda x: {"male": 0, "female": 1}.get(x)
    rec_embarked = lambda x: {"C": 0, "Q": 1, "S": 2}.get(x)
    with open(csv_path) as csv_file:
        df = pd.read_csv(
            filepath_or_buffer=csv_file,
            skipinitialspace=True,
            header=0,
            converters={"Sex": rec_gender, "Embarked": rec_embarked},
            dtype={"Survived": "bool"},
            usecols=['Pclass', 'Sex', 'Age', 'Parch', 'Fare', 'Cabin', 'Embarked', 'SibSp']
        )
    return df


# Paths for the source files
SCRIPT_DIR = pathlib.Path(__file__).parent.resolve()
DATA_PATH = os.path.join(SCRIPT_DIR, "..", "raw/")

# Decide whether to preview the data
SHOW_PREVIEW: Final[bool] = True

# Pre-process test and train data
df_train = pre_process_df(csv_path=os.path.join(DATA_PATH + "train.csv"))
df_test = pre_process_df(csv_path=os.path.join(DATA_PATH + "test.csv"))

# Show generated tables
if SHOW_PREVIEW:
    print("Data path: " + DATA_PATH)
    print("Test data:")
    print(tabulate(df_test.head(), tablefmt="psql", showindex=False, headers=df_test.columns))
    print('Test data column types:')
    print(df_test.dtypes)
    print("Train data:")
    print(tabulate(df_train.head(), tablefmt="psql", showindex=False, headers=df_train.columns))
    print('Train data column types:')
    print(df_train.dtypes)

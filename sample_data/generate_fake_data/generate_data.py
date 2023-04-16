"""Generate Fake Date using Faker"""

import faker
from typing import Final
import datetime
import pandas as pd
from tabulate import tabulate
import random

# Set faker seed
FAKER_SEED: Final[int] = 123
DESIRED_ROWS: Final[int] = 100_000

# Create Faker instance and seed it
fake = faker.Faker()
fake.seed_instance(FAKER_SEED)


def create_fake_rows(num_rows=100):
    res = [
        {
            "name": fake.name(),
            "email": fake.email(),
            "address": fake.address(),
            "credit_card": fake.credit_card_number(),
            "transaction_time": fake.date_time_between(
                start_date=datetime.datetime(2022, 4, 16, 19, 39),
                end_date=datetime.datetime(2023, 4, 16, 19, 39),
            ).isoformat(),
            "tran_amt": random.randint(100,10000)/100.00
        }
        for _ in range(num_rows)
    ]
    return res


df = pd.DataFrame(create_fake_rows(DESIRED_ROWS))
print(tabulate(df.head(n=20), headers="keys", tablefmt="psql"))

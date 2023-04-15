"""Generate Fake Date using Faker"""

import faker
from typing import Final
import random
import pandas as pd
from tabulate import tabulate

# Set faker seed
FAKER_SEED: Final[int] = 123
DESIRED_ROWS: Final[int] = 100_000

# Create Faker instance and seed it
fake = faker.Faker()
fake.seed_instance(FAKER_SEED)

def create_fake_rows(num_rows=100) :
    res = [{
        "name": fake.name(),
        "email": fake.email(),
        "rand_num": random.randint(0, num_rows)
    } for x in range(num_rows)]
    return res

df = pd.DataFrame(create_fake_rows(DESIRED_ROWS))
print(tabulate(df, headers='keys', tablefmt='psql'))

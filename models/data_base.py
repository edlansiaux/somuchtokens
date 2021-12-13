from selenium import webdriver
import pandas as pd
import time
import json
from datetime import datetime
import pathlib
import glob
import sys
sys.path.append(".")
import faker
import numpy as np
import pandas as pd

f = faker.Faker()
token_types = ["HelloBEP20"]
networks = ["Binance Smart Chain", "Binance Smart Chain - Testnet"]

names = [f.bothify(text='???????', letters='ABCDEFGHIJKLMNOPQRSTUVWYXZ') for _ in range(100)]
symbols =  [f.bothify(text='?????', letters='ABCDEFGHIJKLMNOPQRSTUVWYXZ') for _ in range(100)]
token_choices = [np.random.choice(token_types,1)[0] for _ in range(100)]
network_choices = [np.random.choice(networks,1)[0] for _ in range(100)]

database = pd.DataFrame(dict(names=names, symbols=symbols, token_types=token_choices, networks = network_choices))
database.to_csv("submission_form_database.csv", index=False)
database.head()

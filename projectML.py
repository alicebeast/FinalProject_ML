#projectML

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import Any, Callable

train = pd.read_parquet("train.parquet")
test = pd.read_parquet("test.parquet")
sensors = pd.read_parquet("sensors.parquet")

print(sensors)

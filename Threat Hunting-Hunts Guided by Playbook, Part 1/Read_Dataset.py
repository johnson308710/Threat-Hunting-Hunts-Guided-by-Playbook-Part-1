#Read Dataset
import pandas as pd
from pandas.io import json

df = json.read_json(path_or_buf='C:\\Users\\JohnsonSun\\Downloads\\Threat Hunting-Hunts Guided by Playbook, Part 1\\empire_launcher_vbs_2020-09-04160940.json', lines=True)

#印出來
print(df)
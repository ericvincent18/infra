import json
import pandas as pd

f = open("/Users/ericvincent/Downloads/winemag-data-130k-v2.json")

# with open("data_file.json", "r") as read_file:
#     data = json.load(read_file)

data = json.load(f)

df = pd.DataFrame(data)

import pandas as pd

df = pd.read_json('almaty1janto1feb.json')
print(df.components[0]['o3'])
df.to_csv('almaty1janto1feb.csv', header=['Air Quality Index','Components','Time'])
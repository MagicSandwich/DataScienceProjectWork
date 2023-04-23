import os
import pandas as pd

# Define the directory path
directory = 'csv/'

# Get all .csv files in the directory and its subdirectories
csv_files = []
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.csv'):
            csv_files.append(os.path.join(root, file))

# Concatenate all .csv files into a single DataFrame
df = pd.concat((pd.read_csv(file) for file in csv_files), ignore_index=True)

# Write the concatenated DataFrame to a new .csv file
output_file = 'AirPollutionDataset5CitiesKZ.csv'
df.to_csv(output_file, index=False)
print(f'Successfully merged {len(csv_files)} .csv files into {output_file}.')

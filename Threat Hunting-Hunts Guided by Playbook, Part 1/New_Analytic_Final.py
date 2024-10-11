import pandas as pd
from pandas.io import json

# Load the JSON file
df = json.read_json(path_or_buf='C:\\Users\\JohnsonSun\\Downloads\\Threat Hunting-Hunts Guided by Playbook, Part 1\\empire_launcher_vbs_2020-09-04160940.json', lines=True)

# Print the column names for debugging
print("Columns in DataFrame:", df.columns)

# Convert '@timestamp' to datetime format if it's not already
df['@timestamp'] = pd.to_datetime(df['@timestamp'])

# Check if required columns exist
if 'ProcessId' in df.columns:  # 確保 ProcessId 存在
    # Grouping and sorting events by timestamp within process
    df_grouped = df.sort_values(['ProcessId', '@timestamp'])

    # Calculate time differences between events
    df_grouped['time_diff'] = df_grouped.groupby(['ProcessId'])['@timestamp'].diff().dt.total_seconds()

    # Set a threshold for abnormal time differences (10 seconds)
    threshold = 10

    # Filter for anomalies based on time difference
    df_anomalous = df_grouped[df_grouped['time_diff'] > threshold]

    # Replace 'module_name' with a valid column name (e.g., 'Image' or another relevant column)-->【ProcessName】
    def is_sequence_anomalous(ProcessName):
        # Define logic to detect if the sequence is anomalous
        pass  # Replace with your detection logic

    # Apply the function to flag sequence anomalies-->df_grouped['module_name']-->df_grouped['ProcessName']
    df_grouped['is_sequence_anomalous'] = df_grouped['ProcessName'].apply(is_sequence_anomalous)  # 使用正確的列名

    # Combine anomaly flags
    df_final = df_grouped[(df_grouped['time_diff'] > threshold) | (df_grouped['is_sequence_anomalous'])]

    # Output the final results
    print(df_final)
else:
    print("Required columns are missing from the DataFrame.")
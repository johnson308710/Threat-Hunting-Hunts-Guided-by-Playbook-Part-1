import pandas as pd
from pandas.io import json

# Load the JSON file
df = json.read_json(path_or_buf='C:\\Users\\JohnsonSun\\Downloads\\Threat Hunting-Hunts Guided by Playbook, Part 1\\empire_launcher_vbs_2020-09-04160940.json', lines=True)

# Print the column names for debugging
print("Columns in DataFrame:", df.columns)

# Convert '@timestamp' to datetime format if it's not already
df['@timestamp'] = pd.to_datetime(df['@timestamp'])

# Check if required columns exist
if 'ProcessId' in df.columns:  # 這裡改為 ProcessId
    # Grouping and sorting events by timestamp within process
    df_grouped = df.sort_values(['ProcessId', '@timestamp'])  # 這裡改為 ProcessId

    # Calculate time differences between events
    df_grouped['time_diff'] = df_grouped.groupby(['ProcessId'])['@timestamp'].diff().dt.total_seconds()  # 這裡改為 ProcessId

    # Set a threshold for abnormal time differences (10 seconds)
    threshold = 10

    # Filter for anomalies based on time difference
    df_anomalous = df_grouped[df_grouped['time_diff'] > threshold]

    # (Optional) Function to detect anomalous sequences of loaded modules
    def is_sequence_anomalous(module_name):
        # Define logic to detect if the sequence is anomalous
        pass  # Replace with your detection logic

    # Apply the function to flag sequence anomalies
    df_grouped['is_sequence_anomalous'] = df_grouped['module_name'].apply(is_sequence_anomalous)

    # Combine anomaly flags
    df_final = df_grouped[(df_grouped['time_diff'] > threshold) | (df_grouped['is_sequence_anomalous'])]

    # Output the final results
    print(df_final)
else:
    print("Required columns are missing from the DataFrame.")

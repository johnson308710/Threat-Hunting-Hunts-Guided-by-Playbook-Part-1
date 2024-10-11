'''
# Grouping and sorting events by timestamp within process and session
df_grouped = df.sort_values(['process_id', 'session_id', '@timestamp'], ascending=True)

# Calculate time differences between events
df_grouped['time_diff'] = df_grouped.groupby(['process_id', 'session_id'])['@timestamp'].diff().dt.total_seconds()

# Set a threshold for abnormal time differences
threshold = 10  # in seconds

# Filter events where time difference exceeds the threshold
df_anomalous = df_grouped[df_grouped['time_diff'] > threshold]

# Analyze sequence of loaded modules (optional logic can be implemented)
df_grouped['is_sequence_anomalous'] = df_grouped['module_name'].apply(lambda x: detect_anomalous_sequence(x))

# Combine anomaly flags
df_final = df_grouped[(df_grouped['time_diff'] > threshold) | (df_grouped['is_sequence_anomalous'])]
'''
import pandas as pd
from pandas.io import json

# Load the JSON file
df = json.read_json(path_or_buf='C:\\Users\\JohnsonSun\\Downloads\\Threat Hunting-Hunts Guided by Playbook, Part 1\\empire_launcher_vbs_2020-09-04160940.json', lines=True)

# Convert '@timestamp' to datetime format if it's not already
df['@timestamp'] = pd.to_datetime(df['@timestamp'])

# Grouping and sorting events by timestamp within process and session
df_grouped = df.sort_values(['process_id', 'session_id', '@timestamp'])

# Calculate time differences between events
df_grouped['time_diff'] = df_grouped.groupby(['process_id', 'session_id'])['@timestamp'].diff().dt.total_seconds()

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

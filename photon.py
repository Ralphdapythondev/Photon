import streamlit as st
import pandas as pd
import json

# Sample datasets for demo purposes
datasets = {
    'files': list(files),
    'intel': list(intel),
    'robots': list(robots),
    'custom': list(custom),
    'failed': list(failed),
    'internal': list(internal),
    'scripts': list(scripts),
    'external': list(external),
    'fuzzable': list(fuzzable),
    'endpoints': list(endpoints),
    'keys': list(keys)
}

# Function to convert data to JSON
def export_as_json(datasets):
    return json.dumps(datasets, indent=4)

# Function to convert data to CSV (flattening the dictionary to DataFrame first)
def export_as_csv(datasets):
    # Converting dict of lists into a dataframe
    df = pd.DataFrame({key: pd.Series(value) for key, value in datasets.items()})
    return df.to_csv(index=False)

# Allow user to choose export format
export_format = st.selectbox("Choose export format", ["JSON", "CSV"])

# Exporting data based on user's choice
if export_format == "JSON":
    json_data = export_as_json(datasets)
    st.download_button(label="Download JSON", data=json_data, file_name="data.json", mime="application/json")
elif export_format == "CSV":
    csv_data = export_as_csv(datasets)
    st.download_button(label="Download CSV", data=csv_data, file_name="data.csv", mime="text/csv")

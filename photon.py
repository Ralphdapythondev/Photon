import streamlit as st
import pandas as pd
import json
import time
import re
import requests
import warnings
import random
from urllib.parse import urlparse
from core.utils import (luhn, proxy_type, is_good_proxy, top_level, extract_headers, verb, is_link, entropy, regxy, remove_regex, timer, writer)
from core.flash import flash
from core.config import INTELS
from core.mirror import mirror
from core.requester import requester
from core.regex import rintels, rendpoint, rhref, rscript, rentropy
from core.zap import zap
from core.prompt import prompt
from core.updater import updater

warnings.filterwarnings('ignore')

# Streamlit UI for user inputs
st.title('Photon Web Crawler')

# Inputs for the user
main_inp = st.text_input("Root URL")
cookie = st.text_input("Cookie (optional)")
regex = st.text_input("Regex pattern (optional)")
output_dir = st.text_input("Output directory", value="output")
level = st.number_input("Levels to crawl", min_value=1, max_value=10, value=2)
threads = st.number_input("Number of threads", min_value=1, max_value=10, value=2)
delay = st.number_input("Delay between requests (seconds)", min_value=0.0, step=0.1, value=0.0)
timeout = st.number_input("HTTP request timeout (seconds)", min_value=1.0, step=0.5, value=6.0)
verbose = st.checkbox("Verbose output")
clone = st.checkbox("Clone the website locally")
extract_keys = st.checkbox("Find secret keys")

# Initialize datasets
files = set()
intel = set()
robots = set()
custom = set()
failed = set()
internal = set()
scripts = set()
external = set()
fuzzable = set()
endpoints = set()
keys = set()

# Function to run the crawling process
def run_crawl():
    if not main_inp:
        st.error("Please enter a root URL.")
        return

    # Add the root URL to internal set
    internal.add(main_inp)

    # Crawl and extract data as per user options
    # Placeholder for actual crawling logic
    st.write(f"Crawling started for {main_inp}")

    # Simulate some crawling process with time delay
    time.sleep(2)

    # Simulate adding some results (for demo purposes)
    internal.add(f"{main_inp}/example")
    external.add(f"https://external.com")
    files.add(f"{main_inp}/file.pdf")
    intel.add(f"{main_inp}: email@example.com")
    scripts.add(f"{main_inp}/script.js")
    endpoints.add(f"{main_inp}/api/endpoint")

    st.write("Crawling completed.")

# Button to start crawling
if st.button("Start Crawling"):
    run_crawl()

# Export Functionality
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

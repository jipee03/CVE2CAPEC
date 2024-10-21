import os 
import requests
import json
import pandas as panda

TECHNIQUES_FILE_URL = "https://attack.mitre.org/docs/enterprise-attack-v15.1/enterprise-attack-v15.1-techniques.xlsx"
TECHNIQUES_FILE = "resources/techniques_db.json"

# Download the techniques data
def download_techniques():
    try:
        data = panda.read_excel(TECHNIQUES_FILE_URL)
        result = {}
        for i in range(0, len(data)):
            result[data.iloc[i, 0]] = data.iloc[i, 9].split(", ")
        return result
    except Exception as e:
        print(f"Error downloading the data: {str(e)}")
        return None


# Save the techniques data to a JSON file
def save_json(data):
    with open(TECHNIQUES_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    

if __name__ == "__main__":
    print("[!] Downloading techniques data...")
    techniques_data = download_techniques()
    if techniques_data:
        print("[!] Saving techniques data...")
        save_json(techniques_data)
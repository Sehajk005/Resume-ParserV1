import json
import os

def load_job_profiles(filepath="job_profile.json"):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Job profile file '{filepath}' not found. Please create it.")
    with open(filepath, "r") as f:
        return json.load(f)

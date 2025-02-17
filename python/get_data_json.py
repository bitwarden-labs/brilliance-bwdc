import json
import logging
import os
import subprocess

from authenticate_cli import session_key
from variables import bw

logging.basicConfig(level=logging.ERROR)
data_json_GUID = '5f85ece9-40db-4444-98c1-b28300b3d841'
attachment_name = 'data.json'
data_json_output = '/home/bwdc/python/output/data.json'

# Set BW_SESSION as environment variable for ongoing use
os.environ["BW_SESSION"] = session_key 

# Sync vault
subprocess.run([bw, "sync"], stdout=subprocess.PIPE, text=True)

# Get data.json from vault item
data_json_attachment = subprocess.run([bw, "get", "attachment", attachment_name, "--itemid", data_json_GUID, "--output", data_json_output])
print(data_json_attachment)

# Log out
subprocess.run([bw, "logout"])

import logging
import os
import subprocess

from get_mp import mp
from variables import bw, BW_CLI_USERNAME, BW_CLIENTID, BW_CLIENTSECRET

logging.basicConfig(level=logging.ERROR)

os.environ["BW_CLIENTID"] = BW_CLIENTID
os.environ["BW_CLIENTSECRET"] = BW_CLIENTSECRET 


# Reset CLI session and authenticate again
subprocess.run([bw, "logout"])
subprocess.run([bw, "login", "--apikey"])

# Obtain bw cli session key
session_key = subprocess.run(
  [bw, "unlock", mp, "--raw"],
  stdout=subprocess.PIPE,
  text=True
).stdout.strip()

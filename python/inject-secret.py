import json
import os
import subprocess

from authenticate_cli import session_key
from variables import bw

os.environ["BW_SESSION"] = session_key 

ad_admin_password_GUID = '0502c417-dbeb-42ed-9fe1-b283009ad284'

ad_admin_pw = subprocess.run(
  [bw, "get", "item", ad_admin_password_GUID ],
  stdout=subprocess.PIPE,
  text=True
).stdout

ad_admin_pw_json = json.loads(ad_admin_pw)
ad_admin_password = ad_admin_pw_json["login"]["password"]

# This print statement is used as a placeholder for the secret injection
# Replace this with whatever logic you need to inject the secret into your application
# In the YouTube published example, a bash script is used, obtaining credentials via the bws binary
print(ad_admin_password)

# It is important to log out to clear the session key from the environment
# This will be automatically obtained again via the authenticate_cli.py script on next run
subprocess.run([bw, "logout"])
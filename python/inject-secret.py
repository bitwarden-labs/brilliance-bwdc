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

print(ad_admin_password)

# Log out
subprocess.run([bw, "logout"])
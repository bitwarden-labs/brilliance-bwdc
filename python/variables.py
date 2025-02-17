import os
from dotenv import load_dotenv

load_dotenv()

bw = os.getenv("BW_PATH")
bwdc = os.getenv("BWDC_PATH")

STATE_FILE_PATH=os.getenv("STATE_FILE_PATH")
BW_API_URL=os.getenv("BW_API_URL")
BW_IDENTITY_URL=os.getenv("BW_IDENTITY_URL")
BW_ORG_ID=os.getenv("BW_ORG_ID")
BW_ACCESS_TOKEN=os.getenv("BW_ACCESS_TOKEN")

BW_CLI_USERNAME=os.getenv("BW_CLI_USERNAME")
BW_CLIENTID=os.getenv("BW_CLIENTID")
BW_CLIENTSECRET=os.getenv("BW_CLIENTSECRET")

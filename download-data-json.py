import logging
import os
from dotenv import load_dotenv
from bitwarden_sdk import BitwardenClient, DeviceType, client_settings_from_dict

load_dotenv()

client = BitwardenClient(
  client_settings_from_dict(
    {
      "api_url": os.getenv("BW_API_URL", "https://api.bitwarden.com"),
      "identityUrl": os.getenv("BW_IDENTITY_URL", "https://identity.bitwarden.com"),
      "deviceType": DeviceType.SDK,
      "userAgent": "bitwarden-sdk-python",
    }
  )
)

# Add logging and set org id
logging.basicConfig(level=logging.DEBUG)
organisation_id = os.getenv("BW_ORG_ID")

# Set state file location
state_path = os.getenv("STATE_FILE_PATH", "/tmp/state.json")

def get_secret_by_uuid(client, uuid):
    secret_response = client.secrets().get_by_ids([uuid])

    # Debug: Show SM response data structure
    print("Type of secret_response.data:", type(secret_response.data))
    print("Content of secret_response.data:", secret_response.data)

    # Check for success and existence of data list
    if secret_response.success and secret_response.data:

        secret_list = secret_response.data.data
        print("Type of secrets_list:", type(secret_list))
        print("Content of secrets_list:", secret_list)

        if len(secret_list) > 0:
            secret = secret_list[0]

            return {
                "id": str(secret.id),
                "key": secret.key,
                "value": secret.value,
                "note": secret.note,
                "organization_id": str(secret.organization_id),
                "creation_date": str(secret.creation_date),
                "revision_date": str(secret.revision_date),
                "project_id": str(secret.project_id)
            }

    return None


# Authenticate with SM Access Token
try:
    client.auth().login_access_token(os.getenv("BW_ACCESS_TOKEN"), state_path)
except Exception as e:
    logging.error(f"Authentication failed: {e}")


mpuid = 'd388b0e7-b85a-4304-aa2a-b28201001731'
mp = get_secret_by_uuid(client=client, uuid=mpuid)

if mp:
    print("Secret Key:", mp["key"])
    print("Secret Value:", mp["value"])
else:
    print("No secret found.")

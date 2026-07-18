import os
import sys

# Make the project root importable when run directly from any directory.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

import bootstrap  # noqa: F401  (ensures project root is importable from any CWD)

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

# Both credential files live in the `tools` package directory.
TOOLS_DIR = os.path.dirname(os.path.abspath(__file__))
CLIENT_SECRET = os.path.join(TOOLS_DIR, "client_secret.json")
TOKEN_PATH = os.path.join(TOOLS_DIR, "token.json")

flow = InstalledAppFlow.from_client_secrets_file(
    CLIENT_SECRET,
    SCOPES
)

creds = flow.run_local_server(port=0)

with open(TOKEN_PATH, "w") as token:
    token.write(creds.to_json())

print(f"Token generated successfully at: {TOKEN_PATH}")
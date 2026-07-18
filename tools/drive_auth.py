# Copyright (C) 2026 Jagadeeswara Rao Patta
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

"""Google Drive authentication (single responsibility: credentials only)."""

import os

from google.oauth2.credentials import Credentials

# token.json lives alongside this module (in the `tools` package).
DEFAULT_TOKEN_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "token.json")


def load_credentials(token_path: str = DEFAULT_TOKEN_PATH) -> Credentials:
    if not os.path.isabs(token_path):
        token_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), token_path
        )

    if not os.path.exists(token_path):
        raise FileNotFoundError(
            f"Google Drive credential file not found: {token_path}\n"
            "Generate it once with:  python tools/gen_token.py  "
            "(requires client_secret.json from Google Cloud Console)."
        )

    return Credentials.from_authorized_user_file(token_path)

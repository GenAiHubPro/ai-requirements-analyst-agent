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

"""Google Drive document source (single responsibility: Drive I/O only)."""

from docx import Document
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from pypdf import PdfReader

from core.abstractions import DocumentSource

_DOCX_MIME = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
_GDOC_MIME = "application/vnd.google-apps.document"


class DriveDocumentSource(DocumentSource):
    def __init__(self, creds):
        self._service = build("drive", "v3", credentials=creds, cache_discovery=False)

    async def list_files(self) -> list:
        results = (
            self._service.files()
            .list(pageSize=20, fields="files(id,name,mimeType)")
            .execute()
        )
        return results.get("files", [])

    async def get_content(self, file_name: str) -> str:
        results = (
            self._service.files()
            .list(q=f"name='{file_name}' and trashed=false", fields="files(id,name,mimeType)")
            .execute()
        )
        files = results.get("files", [])
        if not files:
            raise FileNotFoundError(f"File '{file_name}' not found in Google Drive.")

        file = files[0]
        file_id = file["id"]
        mime_type = file["mimeType"]

        if mime_type == _GDOC_MIME:
            request = self._service.files().export_media(fileId=file_id, mimeType="text/plain")
            return self._download_text(request)

        request = self._service.files().get_media(fileId=file_id)
        content = self._download_bytes(request)

        if mime_type == _DOCX_MIME:
            doc = Document(content)
            return "\n".join(p.text for p in doc.paragraphs)

        if mime_type == "application/pdf":
            reader = PdfReader(content)
            return "\n".join(page.extract_text() or "" for page in reader.pages)

        if mime_type == "text/plain":
            return content.getvalue().decode("utf-8")

        raise ValueError(f"Unsupported file type: {mime_type}")

    @staticmethod
    def _download_text(request) -> str:
        import io

        fh = io.BytesIO()
        _run_download(request, fh)
        return fh.getvalue().decode("utf-8")

    @staticmethod
    def _download_bytes(request):
        import io

        fh = io.BytesIO()
        _run_download(request, fh)
        fh.seek(0)
        return fh


def _run_download(request, fh) -> None:
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()

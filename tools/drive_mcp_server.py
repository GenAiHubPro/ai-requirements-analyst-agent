from fastmcp import FastMCP
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from docx import Document
from pypdf import PdfReader
import io
import os

mcp = FastMCP("GoogleDriveMCP")

creds = Credentials.from_authorized_user_file(
    "token.json"
)

service = build(
    "drive",
    "v3",
    credentials=creds,
    cache_discovery=False
)

@mcp.tool()
def list_files():
    """ Get list of all available files in my drive  """
    print("================ list files called =============")
    results = service.files().list(
        pageSize=20,
        fields="files(id,name,mimeType)"
    ).execute()

    return results["files"]

@mcp.tool()
def get_file_content(file_name: str) -> str:
    """
    Search a file by name in Google Drive and return its text content.
    Supports:
        - Google Docs
        - PDF
        - DOCX
        - TXT
    """

    print("============= get file content called ===============")

    results = service.files().list(
        q=f"name='{file_name}' and trashed=false",
        fields="files(id,name,mimeType)"
    ).execute()

    files = results.get("files", [])

    if not files:
        return f"File '{file_name}' not found."

    file = files[0]

    file_id = file["id"]
    mime_type = file["mimeType"]

    # -----------------------------
    # Google Docs
    # -----------------------------
    if mime_type == "application/vnd.google-apps.document":

        request = service.files().export_media(
            fileId=file_id,
            mimeType="text/plain"
        )

        fh = io.BytesIO()

        downloader = MediaIoBaseDownload(fh, request)

        done = False

        while not done:
            _, done = downloader.next_chunk()

        return fh.getvalue().decode("utf-8")

    # -----------------------------
    # Download file
    # -----------------------------

    request = service.files().get_media(fileId=file_id)

    fh = io.BytesIO()

    downloader = MediaIoBaseDownload(fh, request)

    done = False

    while not done:
        _, done = downloader.next_chunk()

    fh.seek(0)

    # -----------------------------
    # DOCX
    # -----------------------------

    if mime_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":

        doc = Document(fh)

        content = "\n".join(
            p.text
            for p in doc.paragraphs
        )

        return content

    return f"Unsupported file type: {mime_type}"

@mcp.tool()
def create_markdown_file(file_path: str, content: str) -> str:
    """
    Creates a standardized Markdown (.md) file at the specified path.

    Args:
        file_path: The absolute or relative path where the file should be saved (e.g., 'notes.md').
        content: The body text or main contents of the markdown file.
    """

    print(f"Filepath is: {file_path}")

    # Force extension to be .md if it isn't provided
    if not file_path.endswith('.md'):
        file_path += '.md'

    try:

        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(script_dir)
        print(script_dir, project_root)
        target_absolute_path = os.path.abspath(os.path.join(project_root, file_path))

        # Create directories if they don't exist
        os.makedirs(os.path.dirname(target_absolute_path), exist_ok=True)

        # Write the content to the file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        return f"Successfully created markdown file at: {target_absolute_path}"

    except Exception as e:
        return f"Error creating file: {str(e)}"


if __name__ == "__main__":
    mcp.run(
        transport="http"
    )

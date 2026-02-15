from fastmcp import FastMCP
import requests
import os
import base64

mcp = FastMCP("github-server")

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

@mcp.tool()
def list_repo_files(owner: str, repo: str) -> list[str]:
    url = f"https://api.github.com/repos/{owner}/{repo}/contents"
    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()
    return [f["path"] for f in r.json() if f["type"] == "file"]

@mcp.tool()
def read_repo_file(owner: str, repo: str, path: str) -> str:
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    r = requests.get(url, headers=HEADERS)
    r.raise_for_status()
    data = r.json()
    return base64.b64decode(data["content"]).decode("utf-8", errors="ignore")

if __name__ == "__main__":
    mcp.run()

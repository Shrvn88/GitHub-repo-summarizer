import asyncio
import ast
import os
import google.generativeai as genai
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# ============================
# CHANGE THESE
# ============================

OWNER = "Shrvn88"
REPO = "TravelEase"

UV_PATH = r"C:\Users\palik\.local\bin\uv.exe"
SERVER_PATH = r"C:\Users\palik\Desktop\CWH_DataSciance\MCP\github_repo_summarizer\server.py"

# ============================
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

async def main():
    params = StdioServerParameters(
        command=UV_PATH,
        args=["run", SERVER_PATH],
    )

    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:

            # 1. MCP init
            await session.initialize()
            print("MCP initialized")

            # 2. List repo files
            files_result = await session.call_tool(
                "list_repo_files",
                {"owner": OWNER, "repo": REPO},
            )

            files = ast.literal_eval(files_result.content[0].text)

            print("\nREPO FILES:")
            for f in files:
                print("-", f)

            if not files:
                print("No files found.")
                return

            # 3. Read ALL files
            all_content = ""

            for f in files:
                print("Reading:", f)
                res = await session.call_tool(
                    "read_repo_file",
                    {"owner": OWNER, "repo": REPO, "path": f},
                )

                all_content += f"\n\n--- {f} ---\n"
                all_content += res.content[0].text

            print("\nFULL REPO CONTENT:\n")
            print(all_content[:1000])

            # 4. Gemini summary
            prompt = f"""
Summarize this GitHub repository.

Explain:
- What the project does
- Tech stack
- Purpose

Repository content:
{all_content}
"""

            response = model.generate_content(prompt)

            print("\n================ AI SUMMARY ================\n")
            print(response.text)

if __name__ == "__main__":
    asyncio.run(main())

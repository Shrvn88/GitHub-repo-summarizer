# GitHub Repo Summarizer using MCP + FastMCP + uv + Gemini

This project demonstrates a practical implementation of the **Model Context Protocol (MCP)** by building a GitHub repository summarizer.

A custom MCP client communicates with a FastMCP server to dynamically fetch repository files from GitHub, aggregate context, and generate an AI-powered summary using Google Gemini.

The goal of this project is to understand MCP fundamentals such as lifecycle management, tool primitives, context assembly, and client–server orchestration.

---

## 🚀 What This Project Does

- Starts a FastMCP server over STDIO using `uv`
- Exposes GitHub tools via MCP:
  - List repository files
  - Read file contents
- Implements a custom MCP client:
  - Initializes MCP session
  - Discovers tools
  - Fetches repo files dynamically
  - Aggregates context
- Sends combined repository content to Gemini
- Produces an AI-generated summary of the project

This mimics how real agent systems assemble context across tools before calling an LLM.

---

## 🧠 Architecture

    Custom MCP Client (Python)
              ↓
      STDIO Transport (uv)
              ↓
     FastMCP GitHub Server
              ↓
       GitHub REST API
              ↓
       Repository Files
              ↓
      Context Aggregation
              ↓
          Gemini LLM
              ↓
     Human-readable Summary



---

## 🛠 Tech Stack

- Python 3.11+
- MCP (raw ClientSession)
- FastMCP
- uv (process/runtime)
- GitHub REST API
- Google Gemini (for summarization)

---

## 📁 Project Structure

    github_repo_summarizer/
    │
    ├── client.py # Custom MCP client
    ├── server.py # FastMCP GitHub server
    ├── pyproject.toml # Dependencies
    ├── uv.lock
    └── README.md


---

## ✨ Example Output
MCP initialized
REPO FILES:
- README.md
- requirements.txt

================ AI SUMMARY ================

TravelEase is a Flask-based web application that leverages Google Generative AI to assist
users with travel planning and recommendations...

# Build Agents with ADK

This repository contains sample agents built using the Google ADK (Agentic Development Kit).


## Requirements

- Python 3.10 or higher (see `.python-version` for the recommended version)
- [google-adk](https://pypi.org/project/google-adk/) >= 1.1.1
- [python-dotenv](https://pypi.org/project/python-dotenv/) >= 1.1.0

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/krutip7/build-with-adk.git
   cd build-with-adk
   ```
2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```
    OR 

   ```bash
   uv venv
   ``` 

   **Inititalize Virtual Environment:**

   ```bash
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install .
   ```

    OR 

   ```bash
   uv sync
   ```
4. **Configure environment variables:**
   - Copy `.env.example` to `.env` and fill in the required values (e.g., `GOOGLE_API_KEY`).

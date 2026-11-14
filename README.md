https://ai-support.streamlit.app/

# AI Customer Support Assistant

An AI-powered customer support chatbot built using Python, Google Gemini, and Streamlit.

The application answers customer questions using business-specific information, maintains conversation context, and provides an interactive web interface.

## Features

- AI-powered customer support using Google Gemini
- Business-specific responses based on JSON data
- Conversation history and contextual follow-up questions
- Separate chat sessions for individual visitors
- Interactive web interface built with Streamlit
- Configurable business information, including services, prices, and opening hours

## Tech Stack

- **Python** — Backend application logic
- **Google Gemini API** — AI-generated responses
- **Streamlit** — Web interface
- **JSON** — Business information storage
- **Git & GitHub** — Version control

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-customer-support-assistant.git
cd ai-customer-support-assistant
```

### 2. Install dependencies

Install [uv](https://docs.astral.sh/uv/) if necessary, then run:

```bash
uv venv
uv pip install --python .venv google-genai python-dotenv streamlit
```

### 3. Configure your API key

Create a `.env` file in the project directory:

```env
GEMINI_API_KEY=your_api_key_here
```

Get your API key from [Google AI Studio](https://aistudio.google.com/api-keys).

### 4. Run the application

```bash
uv run --no-project --python .venv -m streamlit run web.py
```

The application will open in your browser.

## Project Structure

```text
ai-customer-support-assistant/
├── main.py          # Terminal interface
├── web.py           # Streamlit web interface
├── chatbot.py       # Gemini API integration
├── business.py      # Business data loader
├── business.json    # Business information
├── .gitignore
└── README.md
```

## Current Limitations

- Business information must be updated manually in JSON.
- Conversations are stored temporarily in browser session state.
- AI-generated answers should be verified before use in production.
- Authentication and persistent storage are not yet implemented.

## Planned Improvements

- Business owner dashboard
- Document uploads and retrieval-augmented generation (RAG)
- Persistent database storage
- Automated testing
- Cloud deployment

## Project Status

**In active development** — Functional prototype.

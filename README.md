# Discord AI Agent

An intelligent AI-powered Discord assistant built with Python that can answer user questions, reason using LLMs, and fetch real-time internet information through external tool integration.

---

## Features

- Responds to Discord messages in real time
- AI reasoning powered by Gemini LLM
- Real-time internet search using Tavily API
- Agent-based architecture using LangChain
- Async event-driven processing
- Tool calling for dynamic information retrieval

---

## Tech Stack

- Python
- Discord.py
- LangChain
- Gemini API
- Tavily Search API
- python-dotenv

---

## Architecture

```text
User Message (Discord)
        ↓
Discord Event Listener
        ↓
AI Agent (LangChain)
        ↓
Tool Selection Logic
        ↓
Tavily Web Search API
        ↓
Gemini Model Processing
        ↓
Response Sent Back To Discord
```

---

## Project Structure

```bash
discord-ai-agent/
│
├── main.py
├── agent.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Environment Variables

Create a `.env` file.

```env
DISCORD_BOT_TOKEN=your_discord_token
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## Installation

Clone repository

```bash
git clone your_repository_url
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run bot

```bash
python main.py
```

---

## Future Improvements

- Voice interaction support
- Long-term conversation memory
- Slash command integration
- Multi-server deployment
- Better agent planning system

---

## Learning Note

Built while learning AI agent architecture, Discord bot development, and real-world LLM tool integration through hands-on implementation.

---

## Author

Abhinandan
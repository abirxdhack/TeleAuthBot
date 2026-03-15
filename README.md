# TeleAuthBot

A fast, lightweight Telegram bot for session-based OTP capture supporting both **Telethon** and **Pyrogram** userbots. All sessions run fully **in-memory** — nothing is ever written to disk.

<br>

## Features

- Supports both **Telethon** and **Pyrogram** session strings
- **In-memory only** — zero disk writes, no leftover session files
- Real-time **OTP polling** from `777000` (Telegram's official OTP sender)
- Per-user state machine with clean wipe & disconnect
- Bot session itself also runs in-memory via `StringSession`

<br>

## Project Structure

```
TeleAuthBot/
├── main.py
├── config.py
├── requirements.txt
├── pyproject.toml
└── utils/
    ├── __init__.py
    └── logger.py
```

<br>

## Prerequisites

- Python **3.10** or higher
- A Telegram Bot Token from [@BotFather](https://t.me/BotFather)
- Telegram `API_ID` and `API_HASH` for the **bot** from [my.telegram.org](https://my.telegram.org)

<br>

## Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/abirxdhack/TeleAuthBot
cd TeleAuthBot
```

### 2. Create a Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or using pyproject.toml:

```bash
pip install .
```

### 4. Configure the Bot

Open `config.py` and fill in your values:

```python
BOT_TOKEN = "your_bot_token_here"
BOT_API_ID = your_api_id_here
BOT_API_HASH = "your_api_hash_here"
```

| Variable | Description |
|---|---|
| `BOT_TOKEN` | Bot token from @BotFather |
| `BOT_API_ID` | API ID from my.telegram.org (for the bot) |
| `BOT_API_HASH` | API Hash from my.telegram.org (for the bot) |
| `OTP_SENDER_ID` | `777000` — Telegram's official OTP sender, do not change |
| `OTP_TIMEOUT` | Seconds to wait for OTP before timing out (default: `60`) |
| `POLL_INTERVAL` | Polling interval in seconds (default: `1.5`) |

### 5. Run the Bot

```bash
python main.py
```

<br>

## Usage

1. Start the bot with `/start`
2. Choose **⚡ Telethon** or **✂️ Pyrogram** from the menu
3. Send your `API_ID`
4. Send your `API_HASH`
5. Send your `SESSION_STRING`
6. Once logged in, press **▶️ Login** to begin OTP polling
7. Send the OTP from your Telegram account — the bot will capture and display it automatically
8. Use **🧹 CleanUp** at any time to disconnect the userbot and wipe state

<br>

## Generating a Session String

If you need to generate a session string first, use one of the following:

**Telethon:**
```python
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print(client.session.save())
```

**Pyrogram:**
```python
from pyrogram import Client

with Client(name="my_account", api_id=API_ID, api_hash=API_HASH) as app:
    print(app.export_session_string())
```

<br>

## Running with systemd (Linux VPS)

Create a service file at `/etc/systemd/system/teleauthbot.service`:

```ini
[Unit]
Description=TeleAuthBot
After=network.target

[Service]
Type=simple
WorkingDirectory=/path/to/TeleAuthBot
ExecStart=/path/to/venv/bin/python main.py
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Then enable and start it:

```bash
sudo systemctl daemon-reload
sudo systemctl enable teleauthbot
sudo systemctl start teleauthbot
sudo systemctl status teleauthbot
```

<br>

## Running with Docker

Create a `Dockerfile`:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "main.py"]
```

Build and run:

```bash
docker build -t teleauthbot .
docker run -d --name teleauthbot teleauthbot
```

<br>

## Notes

- The bot uses `StringSession()` for its own connection — no `bot_session.session` file is created
- Pyrogram userbots are initialized with `in_memory=True` — no `.session` files created
- Telethon userbots use `StringSession(ss)` — also fully in-memory
- Each user's state is isolated; multiple users can operate simultaneously

<br>

## License

MIT License — see [LICENSE](LICENSE) for details.

<br>

## Author

**abirxdhack** — [github.com/abirxdhack](https://github.com/abirxdhack)
### Under development!

## Telegram Weather Bot

Asynchronous Telegram bot for weather information using aiogram 3.x and WeatherAPI.

### Structure
- `bot/` — handlers and keyboards
- `config/` — settings via pydantic
- `db_files/` — SQLAlchemy models and engine **(under development)**
- `modules/` — HTTP client and weather API

### Setup
```bash
pip install -r requirements.txt
cp .env.example .env  # Configure tokens
python bot.py
```

**Note:** Database under development.
🌤️ Weather bot

![List of menu buttons (their labels and order)](image/bot_weather.jpg)

Telegram bot providing up-to-date weather information in any city.

## Features

🔍- Real-time weather data via OpenWeatherMap API
🌡️- Temperature in Celsius with information on how it feels
📝- English weather description
⚡- Easy city name input

📋 Requirements

- Python 3.7+
- aiogram
- aiohttp

## Setup

1. Install dependencies:
```bash
pip install aiogram aiohttp
```

2. Create `config.py`:
```python
YOUR_TOKEN = "your_telegram_bot_token"
WEATHER_API_KEY = "your_openweathermap_api_key"
```

3. Run the bot:
```bash
python weather_bot.py
```

## Usage

1. Start a chat with `/start`
2. Send any city name to get weather information

**Note:** Add `config.py` to `.gitignore` to protect your API keys.
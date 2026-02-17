"""
Weather handler: responds to city names with current weather data.
"""

from aiogram import Router, F
from aiogram.types import Message


from modules import get_weather

CITIES = [
    "Kyiv",
    "Dnipro",
    "Kryvyi Rih",
    "Poltava",
    "Cherkasy",
    "Zhytomyr",
    "Kremenchuk",
    "Bila Tserkva",
    "Uman",
    "Chernivtsi",
    "Pervomaisk"
]


weather_router = Router()


@weather_router.message(F.text.in_(CITIES))
async def handler(message: Message):
    """Fetch and display weather for selected city."""
    data = await get_weather(message.text)
    await message.answer(f"{data['city']}\n{data['temp']}°C\n{data['cont']}")
    

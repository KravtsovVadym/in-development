"""
This module contains handlers for incoming messages.
"""

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.keyboards import key_city


message_router = Router()


@message_router.message(Command("start"))
async def start_handler(message: Message):
    """Handle /start command: show city selection keyboard."""
    await message.answer("Select a city to get the weather:", reply_markup=key_city())

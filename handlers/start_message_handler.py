import text
import kb

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    print(kb.start_keyboard.copy())
    await message.answer(text=text.start_message.format(name=message.from_user.first_name), 
                         reply_markup=kb.start_keyboard)
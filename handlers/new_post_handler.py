import text
import kb

from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(F.text == 'Создать пост')
@router.message(Command('newpost'))
async def create_new_post(message: Message):
    await message.answer(text=text.create_new_post_text)
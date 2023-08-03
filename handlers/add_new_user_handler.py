from aiogram import Router
from aiogram.types import Message, ChatJoinRequest
from aiogram.filters import Command

router = Router()

@router.chat_join_request()
async def add_new_user(update: ChatJoinRequest):
    print('test')
    await update.approve()
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

start_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Создать пост'), KeyboardButton(text='Изменить пост')]
], resize_keyboard=True)

delete_caption_button = InlineKeyboardButton(text='Удалить описание', callback_data='delete_caption')
edit_text_button = InlineKeyboardButton(text='Изменить текст', call_back='edit_text')
add_url_button = InlineKeyboardButton(text='URL-кнопки', call_back='add_url_button')

edit_text_post = InlineKeyboardMarkup(inline_keyboard=[
    [edit_text_button],
    [add_url_button]
])

edit_media_post = InlineKeyboardMarkup(inline_keyboard=[
    [delete_caption_button],
    [edit_text_button],
    [add_url_button]
])
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_start_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text='Подписаться', url='https://t.me/divagerussia')
    kb.button(text='Уже подписан', callback_data='subscribed')
    return kb.as_markup()
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.models.lipstcick import ContourMode, SHADES


def get_start_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()

    kb.button(text='Подписаться', url='https://t.me/divagerussia')
    kb.button(text='Уже подписан', callback_data='subscribed')
    kb.adjust(1)
    return kb.as_markup()


def get_contour_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()

    kb.button(text='Одноцветное', callback_data='monochrome')
    kb.button(text='С контурингом другого цвета', callback_data='contoured')
    kb.adjust(1)
    return kb.as_markup()


def get_shades_kb(mode: ContourMode) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()

    for shade_name, shade_value in SHADES.items(): kb.button(text=shade_name, callback_data=f'{shade_value}_{mode}')
    kb.adjust(1)
    return kb.as_markup()


def get_texture_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()

    kb.button(text='Глянцевая', callback_data='glossy')
    kb.button(text='Матовая', callback_data='matte')
    return kb.as_markup()
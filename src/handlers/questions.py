from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.exceptions import TelegramBadRequest

from src.app import bot
from src.keyboards.for_questions import get_start_kb

CHANNEL_ID = '@nsbxjxnc'

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Это чат бот для онлайн примерки помады Divage. Чтобы продолжить, подпишись на наш канал.",
        reply_markup=get_start_kb()
    )


@router.callback_query(lambda c: c.data in ['subscribed'])
async def process_start_button(callback_query: CallbackQuery):
    response_text = ''

    try:
        if (await bot.get_chat_member(
                CHANNEL_ID,
                callback_query.from_user.id
        )).status not in ['member', 'administrator', 'creator']:
            response_text = 'Не смогли найти вас среди подписчиков канала.'
        else:
            response_text = 'Отлично! Теперь пришли свое селфи для примерки (лицо и губы должно быть хорошо видно, светлое фото в хорошем качестве)'
    except TelegramBadRequest as e:
        if 'member list is inaccessible' in str(e):
            response_text = 'Бот не может проверить подписку. Необходимо пригласить его как администратора в канал.'

    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, response_text)

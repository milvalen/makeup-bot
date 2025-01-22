import os

from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext
from aiogram.types import InputFile, FSInputFile

from src.app import bot
from src.const.const import CHANNEL_ID
from src.keyboards.for_questions import get_shades_kb
from src.models.lipstcick import ContourMode, LipstickSelection


async def is_user_subscribed(user_id: int) -> bool:
    try:
        if (await bot.get_chat_member(CHANNEL_ID, user_id)).status in ['member', 'administrator', 'creator']:
            return True
        else:
            await bot.send_message(user_id, 'Не смогли найти вас среди подписчиков канала.')
    except TelegramBadRequest as e:
        if 'member list is inaccessible' in str(e):
            await bot.send_message(
                user_id,
                'Бот не может проверить подписку. Необходимо пригласить его как администратора в канал.'
            )

    return False


async def send_colors(user_id: int, mode: ContourMode, state: FSMContext):
    await bot.send_message(
        user_id,
        'Выбери оттенок' + (', который хочешь примерить' if mode != 'CONTOUR' else ' для контуринга')
    )

    await bot.send_photo(
        user_id,
        FSInputFile(f'{os.getcwd()}/public/matte-sensuality.jpg'),
        reply_markup=get_shades_kb(mode)
    )

    await state.set_state(LipstickSelection.shade if mode == 'SHADE' else LipstickSelection.contour)
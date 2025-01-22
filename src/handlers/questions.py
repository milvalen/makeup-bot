from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from src.app import bot
from src.keyboards.for_questions import get_start_kb, get_contour_kb, get_texture_kb
from src.models.lipstcick import LipstickSelection
from src.utils.utils import is_user_subscribed, send_colors

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Это чат бот для онлайн примерки помады Divage. Чтобы продолжить, подпишись на наш канал.",
        reply_markup=get_start_kb()
    )


@router.callback_query(lambda c: c.data in ['subscribed'])
async def process_start_button(callback_query: CallbackQuery):
    if not await is_user_subscribed(callback_query.from_user.id): return
    await bot.answer_callback_query(callback_query.id)

    await bot.send_message(
        callback_query.from_user.id,
        'Отлично! Теперь пришли свое селфи для примерки (лицо и губы должно быть хорошо видно, светлое фото в хорошем '
        'качестве)'
    )


@router.message()
async def handle_message(message: Message):
    if not await is_user_subscribed(message.from_user.id): return

    if message.photo:
        await message.answer('Выбери вид нанесения', reply_markup=get_contour_kb())
        return

    await message.answer(
        'Для примерки помады необходимо отправить свое селфи. Лицо и губы должно быть хорошо видно, светлое фото в '
        'хорошем качестве)'
    )


@router.callback_query(lambda c: c.data in ['monochrome', 'contoured'])
async def process_shade(callback_query: CallbackQuery, state: FSMContext):
    if not await is_user_subscribed(callback_query.from_user.id): return
    await bot.answer_callback_query(callback_query.id)

    await send_colors(
        callback_query.from_user.id, 'MONOCHROME' if callback_query.data == 'monochrome' else 'SHADE',
        state
    )


@router.callback_query(lambda c: c.data.endswith(('_MONOCHROME', '_SHADE', '_CONTOUR')))
async def process_texture(callback_query: CallbackQuery, state: FSMContext):
    if not await is_user_subscribed(callback_query.from_user.id): return

    if callback_query.data.endswith('_SHADE'):
        await send_colors(callback_query.from_user.id, 'CONTOUR', state)
        return

    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Выбери текстуру помады', reply_markup=get_texture_kb())
    await state.set_state(LipstickSelection.texture)

@router.callback_query(lambda c: c.data in ['glossy', 'matte'])
async def process_picture(callback_query: CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Помада выбрана!')
    # todo: manage lipstick state

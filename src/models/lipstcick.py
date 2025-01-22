from typing import Literal

from aiogram.fsm.state import StatesGroup, State

SHADES = {
    '01. Бежевый': 'beige',
    '02. Светловато-розовый': 'lightpink',
    '03. Розовато-серый': 'pinky_gray',
    '04. Персиковый': 'peach',
    '05. Пастельно-розовый': 'pale_pink',
    '06. Розовый': 'pink',
    '07. Глубокий розовый': 'deep_pink',
    '08. Ярко-розовый': 'bright_pink',
    '09. Ягодный': 'berry',
    '10. Терракотовый': 'terracotta',
    '11. Тёмно-красный': 'dark_red',
    '12. Винный': 'wine',
}

ContourMode = Literal['MONOCHROME', 'SHADE', 'CONTOUR']

class LipstickSelection(StatesGroup):
    shade = State()
    contour = State()
    texture = State()

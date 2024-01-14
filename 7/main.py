from pathlib import Path
from loguru import logger
import sys
import re
from collections import deque


smalls = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
bigs = smalls.upper()
list_s = list()
list_b = list()
for ch in smalls:
    list_s.append(ch)
for ch in bigs:
    list_b.append(ch)


def initlogger() -> None:
    logger.remove(0)
    logger.add(
        Path(__file__).parents[0].joinpath('errors.log'),
        format='{time} | {level} | {message}',
        encoding='utf8',
        level='ERROR',)
    logger.add(
        sys.stdout,
        format='{time} | {message}',
        level='INFO',)
    with open(Path(__file__).parents[0].joinpath('errors.log'), 'w'):
        pass


def read_shift() -> int:
    while True:
        userdata = input('Введите число смещения: ')
        if len(re.sub(r'-?\d+', '', userdata, count=1)) > 0:
            logger.error(f'Некорректный ввод: {userdata}')
            continue
        else:
            break
    return int(userdata)


def read_text() -> str:
    text = ''
    while True:
        text = input('Введите сообщение: ')
        if len(text) == 0:
            logger.error('Пустая строка сообщения')
            continue
        break
    return text


def encode(s: str, shift: int) -> str:
    def shifter(ch: str, lst: list) -> str:
        n = lst.index(ch)
        dq = deque(lst)
        dq.rotate(shift)
        return dq[n]
    res_s = ''
    for ch in s:
        if ch in list_s:
            res_s += shifter(ch, list_s)
        elif ch in list_b:
            res_s += shifter(ch, list_b)
        else:
            res_s += ch
    return res_s


def decode(s: str, shift: int) -> str:
    return encode(s, 0 - shift)


if __name__ == '__main__':

    initlogger()
    shift = 0 - read_shift()
    text = read_text()

    encoded = encode(text, shift)
    logger.info(f'Шифрованное сообщение {encoded}')
    logger.info(f'Расшифрованное сообщение {decode(encoded, shift)}')

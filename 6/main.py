from pathlib import Path
import re
from loguru import logger
import sys


def goodline(i: int, s: str) -> str:
    s = re.sub(r'\n', '', s)

    xstr = re.sub(r'[0-9]|\*|/|\+|-|\.|\s', '', s)
    if len(xstr) > 0:
        logger.error(f'№{i}>>> Не поддерживаемые сымволы: {xstr}')
        return ''

    xstr = re.search(r'\d\s+\d', s)
    if xstr is not None:
        logger.error(f'№{i}>>> Не указано действие с числами')
        return ''

    s = re.sub(r'\s', '', s)

    if len(s) == 0:
        logger.error(f'№{i}>>> Пустая строка')
        return ''

    return s


def calc_one(ab: list, act: str, i: int) -> None:
    if act == '+' or act == '':
        print(f'№{i} {ab[0]} {"+ " if ab[1][0]!="-" else ""}{ab[1]} = {float(ab[0]) + float(ab[1])}')
    if act == '*':
        print(f'№{i} {ab[0]} * {ab[1]} = {float(ab[0]) * float(ab[1])}')
    if act == '/':
        if float(ab[1]) == 0:
            logger.error(f'№{i}>>> Деление на 0')
        else:
            print(f'№{i} {ab[0]} / {ab[1]} = {float(ab[0]) / float(ab[1])}')


def calc_all(textlist) -> None:
    for i, textline in enumerate(textlist, 1):
        if goodstr := goodline(i, textline):
            regex = re.compile(r'-?\d+\.?\d*')
            match = re.findall(regex.pattern, goodstr)
            if len(match) != 2:
                logger.error(f'№{i}>>> Поддерживаются операции только в одно действие')
                continue
            calc_one(
                match,
                re.sub(regex.pattern, '', goodstr),
                i)


if __name__ == '__main__':
    logger.remove(0)
    logger.add(
        Path(__file__).parents[0].joinpath('errors.log'),
        format='{time}|{level}|{message}',
        encoding='utf8',
        level='ERROR',)
    with open(Path(__file__).parents[0].joinpath('errors.log'), 'w') as f:
        pass
    if Path(__file__).parents[0].joinpath('exprs.txt').is_file():
        with open(Path(__file__).parents[0].joinpath('exprs.txt'), 'r') as f:
            calc_all(f.readlines())
    else:
        print('Нет файла данных, запуск приложения не возможен...')

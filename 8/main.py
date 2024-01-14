from pathlib import Path
from loguru import logger
import sys
import re
from datetime import datetime, timedelta
import pprint


def initlogger() -> None:
    logger.remove(0)
    logger.add(
        Path(__file__).parents[0].joinpath('logs.log'),
        format='{time} | {level} | {message}',
        encoding='utf8',
        level='DEBUG',)
    logger.add(
        sys.stdout,
        format='{time} | {message}',
        level='INFO',)
    with open(Path(__file__).parents[0].joinpath('logs.log'), 'w'):
        pass


class Bass:

    def __init__(self):
        self.athlets = dict()

    def write(self, s: str) -> None:
        arr = str.split(re.sub(r'\n', '', s), ',')
        if arr[1] not in self.athlets.keys():
            self.athlets[arr[1]] = dict()
        if arr[2] not in self.athlets[arr[1]]:
            self.athlets[arr[1]][arr[2]] = {'In': None, 'Out': None}
        self.athlets[arr[1]][arr[2]][arr[3]] = datetime.strptime(arr[0], '%d/%m/%Y %H:%M:%S')

    def calc(self):
        for atlt in self.athlets.keys():
            # print(atlt)
            for locs in self.athlets[atlt].keys():
                # print('  ', locs)
                # pprint.pprint(self.athlets[atlt][locs])
                if self.athlets[atlt][locs]['In'] is None:
                    logger.debug(f'Не зафиксировано время входа {atlt} в {locs}')
                if self.athlets[atlt][locs]['Out'] is None:
                    logger.debug(f'Не зафиксировано время выхода {atlt} в {locs}')
                if self.athlets[atlt][locs]['In'] and self.athlets[atlt][locs]['Out']:
                    td: timedelta = self.athlets[atlt][locs]['Out'] - self.athlets[atlt][locs]['In']
                    logger.info('Атлет {a} провёл в {l}: {t} мин.'.format(
                        a=atlt,
                        l=locs,
                        t=round(td.seconds / 60),
                    ))


def runprog(lines: list) -> None:
    lines.pop(0)
    bass = Bass()
    for line in lines:
        bass.write(line)
    bass.calc()


if __name__ == '__main__':
    initlogger()
    if Path(__file__).parents[0].joinpath('activity.csv').is_file():
        with open(Path(__file__).parents[0].joinpath('activity.csv'), 'r') as f:
            runprog(f.readlines())
    else:
        print('Нет файла данных, запуск приложения не возможен...')

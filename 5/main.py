inputdata = ['H2-S-O4', 'H2-O', 'NA-CL', 'H-CL', 'K-CL']

table = {
    'H': 1.008,
    'O': 15.999,
    'S': 32.066,
    'NA': 22.990,
    'CL': 35.453,
    'K': 39.098,
}


def calcone(s: str) -> float:
    el: str = ''
    cnt: str = ''
    for ch in s:
        if ch.isdigit():
            cnt += ch
        else:
            el += ch
    if not cnt:
        return table[el]
    else:
        return table[el] * int(cnt)


for item in inputdata:
    print('{t} {v:.3f}'.format(
        t=item,
        v=sum(map(calcone, item.split('-')))
    ))

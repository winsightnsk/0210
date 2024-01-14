import math


def radius(x: float, y: float) -> float:
    return (x * x + y * y)**(0.5)


def phi(x: float, y: float) -> float:
    if (x > 0):
        return math.atan2(y, x)
    if (x < 0 and y > 0):
        return math.pi + math.atan2(y, x)
    if (x < 0 and y < 0):
        return math.atan2(y, x) - math.pi
    if (x == 0 and y > 0):
        return math.pi / 2.0
    if (x == 0 and y < 0):
        return math.pi / -2.0


x, y = 10, -33

print('Полярный радиус: radius={r:.3f}\nПолярный угол: phi={u:.3f}'.format(
    r=radius(x, y),
    u=phi(x, y)
))

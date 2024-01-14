import math


def gen_sin(x) -> float:
    k = 0
    while True:
        yield (-1)**k * x**(2 * k + 1) / math.factorial(2 * k + 1)
        k += 1


def gen_cos(x) -> float:
    k = 0
    while True:
        yield (-1)**k * x**(2 * k) / math.factorial(2 * k)
        k += 1


def gen_exp(x) -> float:
    n = 0
    while True:
        yield (x ** n) / math.factorial(n)
        n += 1


x = 1
rlen = 5
genexp = gen_exp(x)
gensin = gen_sin(x)
gencos = gen_cos(x)

print('math.sin({x}) - sin({x}) = {calce:.1e}'.format(
    x=x,
    calce=math.sin(x) - sum([next(gensin) for _ in range(rlen)])
))
print('math.cos({x}) - cos({x}) = {calce:.1e}'.format(
    x=x,
    calce=math.cos(x) - sum([next(gencos) for _ in range(rlen)])
))
print('math.exp({x}) - exp({x}) = {calce:.1e}'.format(
    x=x,
    calce=math.exp(x) - sum([next(genexp) for _ in range(rlen)])
))

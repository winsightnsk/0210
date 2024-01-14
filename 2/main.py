def get_fib_numbers(qty: int):
    """
    Числа фибоначи\n
    args:
        qty (int): Количество элементов генерируемой последовательности
            Максимум 100 элементов
    return:
        генератор
    """
    if not isinstance(qty, int):
        raise Exception(f'передан не верный формат числа ({type(qty)})')
    if qty < 0:
        raise Exception('количество элементов не может быть отрицательным')
    a, b = 0, 1
    for _ in range(qty if qty < 100 else 100):
        yield a
        a, b = b, a + b


fib_numbers = list(get_fib_numbers(10))
assert len(fib_numbers) == 10
print(fib_numbers)

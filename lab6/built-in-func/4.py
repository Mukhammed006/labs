import time

def test(a, t):
    time.sleep(t/1000)
    b=a**0.5
    print(f'Square root of {a} after {t} miliseconds is {b}')


a, t = float(input('Input:\n')), float(input())
test(a, t)
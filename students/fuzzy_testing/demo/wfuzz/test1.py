def suma(a, b):
    if a < 0 and b < 0:
        return 0
    return a + b

import random

for _ in range(1000):
    a = random.randint(-100,100)
    b = random.randint(-100,100)
    
    try:
        result = suma(a, b)
    except Exception as e:
        print(f"Excepción con entrada: a={a}, b={b}, error={e}")
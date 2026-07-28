import math

lower = 1
upper = 100

phi = (1 + math.sqrt(5)) / 2

n = 1

while True:
    a = math.floor(n * phi)
    b = math.floor(n * phi * phi)

    if a > upper:
        break

    if a >= lower and b <= upper:
        print(f"({a}, {b})")

    n += 1
            
        
    
    

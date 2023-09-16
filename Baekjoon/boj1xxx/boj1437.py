n = int(input())
t = n // 3
d = (n % 3) // 2
if n <= 3:
    print(n)
else:
    if n % 3 == 1:
        t -= 1
        d += 2
    print(((3**t) * (2**d)) % 10007)

#first method
a , b , c = input().split();a = int(a);b = int(b);c = int(c);v = b**2 - a * c *4;ans = "NoSolution"
if v == 0:
    ans = f"DR={b/(-2*a)}"
elif v > 0:
    ans = f"{(-b-v**0.5)/(2*a)} {(-b+v**0.5)/(2*a)}"
print(ans)
# second method
from math import sqrt  # "sqrt" calculates the real square root (with decimals);"isqrt" calculates only the integer part, directly discarding the decimals!

f = lambda a,b,c:b ** 2 - a * c * 4

a, b, c = map(int, input().split())
v = f(a, b, c)
print(f"DR={b / (-2 * a)}" if v == 0 else f"{(-b - sqrt(v)) / (2 * a)} {(-b + sqrt(v)) / (2 * a)}" if v > 0 else "NoSolution")

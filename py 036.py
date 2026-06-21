f = lambda s:s>1 and all(s % i != 0 for i in range(2, int(s**0.5)+1))
def k(y):
    if f(y-1):return y-1
    else:return k(y-1)
for i in range(int(input())):
    print(k(int(input())))
  

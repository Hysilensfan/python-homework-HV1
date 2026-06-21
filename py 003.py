#first method
y=int(input())
ans="Wrong"
if y>2:
    ans=(y-2)*4+21
elif 0<y<=2:
    ans=y*10.5
print(ans)
#second method
y = int(input())
print((y - 2) * 4 + 21 if y > 2 else y * 10.5 if 0 < y <= 2 else "Wrong")

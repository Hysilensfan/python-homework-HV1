from ast import literal_eval as a
print((str(list(map(list,zip(*(a(input())[::-1])))))).replace(" ",""))

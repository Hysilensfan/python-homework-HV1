s = input()
print(f"{s}way" if s[0] in "aeiou" else f"{s[1:]}{s[0]}ay")

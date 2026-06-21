s = input()
print(f"{(s[:-3])}"if (s[0] in "aeiou" or s[1] in "aeiou") and s[-3:] == "way" else f"{(s[-3])+(s[:-3])}")

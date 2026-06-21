def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000
             }
    tot=prev=0
    for c in reversed(s):
        V = roman[c]
        if V < prev:
            tot -= V
        else:
            tot += V
        prev = V
    return tot
for _ in range(int(input())):
    print(roman_to_int(input()))

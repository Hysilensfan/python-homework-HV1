from sys import stdin as s

for line in s:
    test_data = list(map(float, line.split())) # storing data as the double floating.
    test_data = [[test_data[p], test_data[p + 1]] for p in range(0, 8, 2)]  # The processed data ends up in a 2D array format.
    unduplicated = [e for e in test_data if test_data.count(e) == 1]  # get A、B.
    duplicated = next(i for i in test_data if test_data.count(i) == 2)  # get C.
    print(f"{unduplicated[0][0] + unduplicated[1][0] - duplicated[0]:.3f} {unduplicated[0][1] + unduplicated[1][1] - duplicated[1]:.3f}")  # D = A + B - C.

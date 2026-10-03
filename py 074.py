from ast import literal_eval as le


def nesting_doll_maximum(test: list[list[int]]) -> int:
    if len(test) == 1:
        return 1
    test.sort(key=lambda x: (x[0], -x[1]))
    dp: list = [1] * len(test)
    max_count: int = 1
    for i in range(1, len(test)):
        for j in range(i):
            if test[j][0] < test[i][0] and test[j][1] < test[i][1]:
                dp[i]: int = max(dp[i], dp[j] + 1)
        max_count: int = max(max_count, dp[i])
    return max_count


def main() -> None:
    [print(nesting_doll_maximum(le(input()))) for _ in range(int(input()))]
    return


main()
exit(0)

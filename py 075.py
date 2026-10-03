def search_highest(map_: list[list[int]]) -> int:
    n: int = len(map_)
    m: int = len(map_[0])

    def can_reach(min_score: int) -> bool:  # 從左上到右下檢查能否只走 >= min_score 的格子
        visited: set = set()

        def dfs(i: int, j: int) -> bool:
            if i < 0 or i >= n or j < 0 or j >= m:  # 邊界檢查
                return False
            if (i, j) in visited or map_[i][j] < min_score:  # 已訪問或格子值太小
                return False
            visited.add((i, j))
            if i == n - 1 and j == m - 1:
                return True  # 到達終點！
            return (dfs(i + 1, j) or dfs(i - 1, j) or
                    dfs(i, j + 1) or dfs(i, j - 1))  # 東西南北探訪

        return dfs(0, 0)

    left, right = 1, max(
        max(row) for row in map_
    )
    answer: int = 1
    while left <= right:  # 對所有結果進行二元搜尋
        mid = (left + right) // 2
        if can_reach(mid):
            answer = mid
            left: int = mid + 1  # 能走就嘗試更高的
        else:
            right: int = mid - 1  # 不能走就降低要求
    return answer


def main() -> None:
    for _ in range(int(input())):
        row = [
            int(input()) for _ in range(2)
        ][0]  # 第二個為 Column 故取第一個
        maze = [
            list(map(int, input().split()))
            for _ in range(row)
        ]
        print(
            search_highest(maze)
        )


main()
exit(0)


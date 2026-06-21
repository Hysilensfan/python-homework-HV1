for _ in range(int(input())):
    print(((bin(int(input()))).replace("0b","")).zfill(8))

def solution(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                count += 1   # 제곱수면 하나만
            else:
                count += 2   # (i, n//i) 두 개
        i += 1
    return count
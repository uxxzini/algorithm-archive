def solution(n):
    result = []
    d = 2
    
    while d * d <= n:     # d가 n의 제곱근까지만 검사
        if n % d == 0:
            result.append(d)
            while n % d == 0:
                n //= d   # 같은 소인수는 전부 나눠버림
        d += 1
    
    if n > 1:             # 마지막에 남은 수가 소수면 추가
        result.append(n)
    
    return result
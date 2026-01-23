def solution(numbers, k):
    idx = 0
    n = len(numbers)

    for _ in range(k - 1):
        idx = (idx + 2) % n

    return numbers[idx]
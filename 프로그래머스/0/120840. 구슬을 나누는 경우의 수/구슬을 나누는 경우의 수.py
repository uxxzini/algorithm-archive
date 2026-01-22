def solution(balls, share):
    result = 1
    for i in range(1, share + 1):
        result = result * (balls - i + 1) // i
    return result

# import math
# def solution(balls, share):
#     return math.comb(balls, share)
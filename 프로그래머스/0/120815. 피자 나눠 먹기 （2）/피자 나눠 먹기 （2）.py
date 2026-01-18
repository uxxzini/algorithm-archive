# 최소공약수 lcm
# def solution(n):
#     return math.lcm(n, 6) // 6

import math

def solution(n):
    pizza = 1
    while (pizza * 6) % n != 0:
        pizza += 1
    return pizza
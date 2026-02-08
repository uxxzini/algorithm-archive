def solution(order):
    answer = 0
    for x in str(order):
        if x in '369':
            answer += 1
    return answer
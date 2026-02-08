# def solution(array, n):
#     array.sort(key=lambda x: (abs(x - n), x))
#     return array[0]

def solution(array, n):
    answer = array[0]
    
    for x in array:
        if abs(x - n) < abs(answer - n):
            answer = x
        elif abs(x - n) == abs(answer - n) and x < answer:
            answer = x
            
    return answer
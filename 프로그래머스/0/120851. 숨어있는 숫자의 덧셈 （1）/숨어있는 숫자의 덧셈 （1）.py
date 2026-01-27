def solution(my_string):
    total = 0
    
    for ch in my_string:
        if ch.isdigit():   # 숫자 구분
            total += int(ch)
            
    return total
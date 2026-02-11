def solution(my_string, num1, num2):
    s = list(my_string)      # 문자열 → 리스트 변환
    s[num1], s[num2] = s[num2], s[num1]
    return ''.join(s)        # 다시 문자열로 변환
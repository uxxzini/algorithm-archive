def solution(my_string, letter):
    result = ""
    for i in my_string:
        if i != letter:
            result += i
    return result

### 파이썬 내장 함수 활용
# def solution(my_string, letter):
#     return my_string.replace(letter, "")
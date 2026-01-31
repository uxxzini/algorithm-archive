def solution(s):
    stack = []
    
    for x in s.split(): #공백으로 자르기
        if x == "Z":
            stack.pop() #리스트의 맨 마지막 값 삭제
        else:
            stack.append(int(x))
    
    return sum(stack)
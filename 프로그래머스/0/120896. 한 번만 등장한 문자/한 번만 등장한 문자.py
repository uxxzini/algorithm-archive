def solution(s):
    #1 한 번만 등장하는 문자 리스트 만들기
    a = []
    for ch in s:
        if s.count(ch) == 1 :
            a.append(ch)
    #2 정렬하기
    return ''.join(sorted(a))
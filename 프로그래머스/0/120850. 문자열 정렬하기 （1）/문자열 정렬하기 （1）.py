def solution(my_string):
    nums = []
    
    for ch in my_string:
        if ch.isdigit():          # 숫자인지 확인
            nums.append(int(ch))  # 정수로 변환해서 추가
            
    return sorted(nums)
def solution(money):
    price = 5500
    cups = money // price      # 최대 잔 수 (몫)
    change = money % price    # 남는 돈 (나머지)
    return [cups, change]
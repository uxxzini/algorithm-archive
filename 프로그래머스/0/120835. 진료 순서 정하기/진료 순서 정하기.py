def solution(emergency):
    sorted_em = sorted(emergency, reverse=True)  # 큰 값이 먼저 오게 정렬
    return [sorted_em.index(e) + 1 for e in emergency]
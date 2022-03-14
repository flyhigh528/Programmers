def solution(brown, yellow):
    answer = []

    # 카펫 전체 크기 저장
    cnt = brown + yellow
    
    # 카펫 크기의 세로 가로는 = x * y = cnt
    # y의 길이는 x보다 길어야 하기 때문에 cnt 크기 ~ 2까지 y값 확인
    # 가운데 yellow의 갯수가 (x-2) * (y-2)의 값일때 결과값 반환
    for y in range(cnt, 2, -1):
        if cnt%y == 0:
            if yellow == (cnt//y-2) * (y-2):
                return[y, cnt//y]


solution(10, 2)
solution(8, 1)
solution(24, 24)
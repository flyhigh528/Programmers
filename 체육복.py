def solution(n, lost, reserve):
    answer = 0
    cnt = 0
    real_lost= []

    # 테스트 케이스 중 정렬 안된 리스트의 케이스가 있음
    lost.sort()
    reserve.sort()

    # 본인의 여분이 있는경우 제외
    for i in range(len(lost)):
        if reserve.count(lost[i]) > 0:
            print(lost[i], '는 자기 여분이 있어요')
            reserve.remove(lost[i])
            cnt +=1
        else:
            real_lost.append(lost[i])

    # 빌려야 할사람 빌려보기
    for i in range(len(real_lost)):
        print(real_lost[i], '는 체육복 빌려오세요', i)
        for j in range(len(reserve)):
            print(reserve[j], '여분이 있어요', j)
            if real_lost[i] -1 == reserve[j]:
                print('한치수작은거 빌림!')
                cnt += 1
                reserve.remove(real_lost[i] -1)
                break
            elif real_lost[i] + 1 == reserve[j]:
                print('한치수큰거 빌림!')
                cnt += 1
                reserve.remove(real_lost[i] + 1)
                break
    
    return n- len(lost) + cnt


# print(solution(5,[2, 4],[1, 3, 5]))
# print(solution(5, [2, 4], [3]))
print(solution(5, [1, 2, 4], [2,3,4,5]))
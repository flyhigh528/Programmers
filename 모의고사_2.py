def solution(answers):
    answer = []
    tmp_list = []

    no1 = [1,2,3,4,5]
    no2 = [2,1,2,3,2,4,2,5]
    no3 = [3,3,1,1,2,2,4,4,5,5]
    no3 = [5,4,3,2,1]
    no1_correct = 0
    no2_correct = 0
    no3_correct = 0
    no4_correct = 0

    # 채점하기
    for i in range(0,len(answers)):
        if no1[i%5] == answers[i]:
            no1_correct += 1
            
        if no2[i%8] == answers[i]:
            no2_correct += 1
            
        if no3[i%10] == answers[i]:
            no3_correct += 1

        if no3[i%5] == answers[i]:
            no4_correct += 1

    compare = [no1_correct, no2_correct, no3_correct, no4_correct]
    print(compare)
    
    
    for i in range(len(compare)):
        print('현재 값 : {}, 최대값 : {}'.format(compare[i], max(compare)))
        if compare[i] == max(compare):
            answer.append(i+1)
    
    print(answer)
    return answer
    
solution([1, 2, 3, 4, 5])
solution([1,3,2,4,2])
solution([3, 3, 2, 1, 5])
def solution(answers):
    answer = []
    tmp_list = []

    no1 = [1,2,3,4,5]
    no2 = [2,1,2,3,2,4,2,5]
    no3 = [3,3,1,1,2,2,4,4,5,5]
    no1_correct = 0
    no2_correct = 0
    no3_correct = 0
    tmp_score = 99

    # 채점하기
    for i in range(0,len(answers)):
        # print('정답, {}, 넘버원 {}, 넘버투{}. 넘버쓰리{}'.format(answers[i], no1[i%5], no2[i%5], no3[i%10]))
        if no1[i%5] == answers[i]:
            no1_correct += 1
            
        if no2[i%8] == answers[i]:
            no2_correct += 1
            
        if no3[i%10] == answers[i]:
            no3_correct += 1
    
    # 사전형태로 저장
    compare = {1:no1_correct, 2:no2_correct, 3:no3_correct}
    # 점수 높은순으로 정렬하기
    sort_by_score = sorted(compare.items(), key=lambda x : x[1], reverse=True)
    # print(sort_by_score)
    if no1_correct == no2_correct == no3_correct:
        answer = [1,2,3]
    else:
        for i in range(0, len(sort_by_score)):
            if i == 0:
                tmp_list.append(sort_by_score[i][0])

            # 점수가 같을 경우는 리스트에 번호를 넣어 정렬 후 결과값에 넣고
            # 점수가 앞사람 점수와 다를 경우에는
            if sort_by_score[i][1] == 0:
                break
            elif sort_by_score[i-1][1] == sort_by_score[i][1]:
                # print(sort_by_score[i][1], '동일 스코어 리스트 입력, 소팅')
                tmp_list.append(sort_by_score[i][0])
                tmp_list.sort
            else:     
                break
        
        
        answer += tmp_list
    
    print(answer)
    return answer

# 1 2 6 10 11 12
solution([1, 2, 3, 4, 5])
solution([1,3,2,4,2])
solution(	[3, 3, 2, 1, 5])


# 1) - [3, 3, 2, 1, 5] -> [3]
# 2) - [5, 5, 4, 2, 3] -> [1,2,3]
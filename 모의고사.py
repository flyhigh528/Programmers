def solution(answers):
    answer = []

    no1 = [1,2,3,4,5]
    no2 = [2,1,2,3,2,4,2,5]
    no3 = [3,3,1,1,2,2,4,4,5,5]
    no1_correct = 0
    no2_correct = 0
    no3_correct = 0

    for i in range(0,len(answers)):
        print('정답, {}, 넘버원 {}, 넘버투{}. 넘버쓰리{}'.format(answers[i], no1[i%5], no2[i%5], no3[i%10]))
        if no1[i%5] == answers[i]:
            no1_correct += 1
            
        if no2[i%8] == answers[i]:
            no2_correct += 1
            
        if no3[i%10] == answers[i]:
            no3_correct += 1

    print(no1_correct, no2_correct, no3_correct)

    return answer


solution([1, 3, 2, 4, 2])
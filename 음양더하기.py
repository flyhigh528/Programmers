def solution(absolutes, signs):
    answer = 0
    n = 0

    print(len(absolutes))
    
    for i in range(len(absolutes)):
        if signs[i] == True:
            n = absolutes[i]
        else:
            n = int('-' + str(absolutes[i]))    
        
        answer += n
    
    print(answer)
    return answer

solution([4, 7, 12], [True, False, True])    
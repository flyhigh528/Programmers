def solution(s):
    answer = 0
    str_set = {}
    temp = ''
    i = 0
    
    # 반복 문자열의 최대길이는 전체 길이의 1/2까지로 설정
    # 압축에 대한 스코어는 문자열길이 * 갯수로 설정
    # 스코어가 가장 높은 방식의 길이값을 반환
    
    for i in range(0, len(s), i):
        temp = temp + s[i]
        str_set.add(s[i])
        i += 1
        
        
        
       
    return answer


solution("aabbaccc")

solution("ababcdcdababcdcd")
solution("abcabcdede")
solution("abcabcabcabcdededededede")
solution("xababcdcdababcdcd")
def solution(s):
    answer = ''
    num_list = {"zero":'0', "one":'1', "two":'2', "three":'3', "four":'4', "five":'5', 
                "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    eng_num = ''
    
    for input in s:
        if input.isdigit():     
            answer = answer + input
        elif input.isalpha():            
            eng_num = eng_num + input
            if num_list.get(eng_num) != None:
                answer = answer + str(num_list.get(eng_num))
                eng_num = ''

    return int(answer)

print(solution("one4seveneight"))


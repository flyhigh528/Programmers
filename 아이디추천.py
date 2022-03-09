from asyncio.windows_events import NULL
from re import A


def solution(new_id):
    answer = ''
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    Input_id = new_id.lower()
    
    print("1단계 완료값 : ", Input_id)

    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    for id_chr in Input_id:
        if id_chr.isalpha() or id_chr.isdigit() or id_chr == '-' or id_chr == '_' or id_chr == '.' :
            answer += id_chr
            
    print("2단계 완료값 : ", answer)

    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    while answer.find("..") != -1:
        answer = answer.replace("..", ".")
    
    print("3단계 완료값 : ", answer)
    
    # 4-1 단계 new_id에서 마침표(.)가 처음에 위치한다면 제거합니다.
    if answer[0] =='.':
        answer = answer[1:]
    print("4-1단계 완료값:{}.".format(answer))
    
    # 4-2 단계 new_id에서 마침표(.)가 끝에 위치한다면 제거합니다.
    # 6단계에서 재사용을 위해 함수로 생성.
    # 함수 입력값이 공백인경우, 받은값 리턴
    def last_dot_del(str):
        if len(str) > 0:
            if str[len(str)-1] =='.':
                str = str[0:len(str)-1]
        return str
    
    answer = last_dot_del(answer)
    print("4-2단계 완료값:", answer)

    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if answer == "":
        answer = 'a'
    print("5단계 완료값:", answer)
    
    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    # 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(answer) > 15:
        answer = last_dot_del(answer[0:15])        
    print("6단계 완료값:", answer)

    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(answer) <= 2:
        answer = answer.ljust(3, answer[len(answer)-1])   
    print("7단계 완료값:", answer)

    return answer


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
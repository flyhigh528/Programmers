def solution(record):
    answer = []
    list = []
    action = {"Enter":"님이 들어왔습니다.", "Leave":"님이 나갔습니다.", "Change":"님 아이디가 변경되었습니다." }
    on_chat = {}
    # 채팅방 처리정보 LIST형태로 변환
    for cnt in record:
        list.append(cnt.split())

    # print(list)
    # list[0] : action
    # list[1] : id
    # list[2] : nickname
    
    # 입장정보 사전 저장
    for data in list:
        if data[0] == "Enter":
            on_chat[data[1]] = data[2]
        elif data[0] == "Change":
            on_chat[data[1]] = data[2]
    
    # 문구조합 결과값 입력
    for data in list:
        if data[0] == "Enter":
            answer.append(on_chat.get(data[1])+action.get(data[0]))
        elif data[0] == "Leave":
            answer.append(on_chat.get(data[1])+action.get(data[0]))
        # elif data[0] == "Change":
        #     answer.append(on_chat.get(data[1])+action.get(data[0]))

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))

# [['Enter', 'uid1234', 'Muzi'], ['Enter', 'uid4567', 'Prodo'], ['Leave', 'uid1234'], ['Enter', 'uid1234', 'Prodo'], ['Change', 'uid4567', 'Ryan']]

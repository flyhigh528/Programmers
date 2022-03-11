# 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
# k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
# 유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.

def solution(id_list, report, k):
    answer = []
    report_cnt = dict()
    report_send = dict()

    # 1-1. 신고 카운트를 위한 아이디리스트 사전 생성 및 초기화
    for id in id_list:
        report_cnt[id] = 0    
        report_send[id] = 0   
    # print(report_cnt)
    
    # 2-1. 신고중복제거를 위하여 신고 리스트 set 타입으로 변경
    report_list = set(report)
    
    # 2-2. 신고 리스트를 신고리스트에 카운팅
    for list in report_list:
        report_cnt[list.split()[1]] = report_cnt[list.split()[1]] + 1
        
    # 신고 리스트에서 정지된 유저를 신고한 유저 메일 전송
    # 신고결과중에서
    for send in report_cnt:
        # 정지 기준 이상 신고되었으면
        if report_cnt[send] >= k:
            # print("{}가 신고누적 {}번으로 정지되었습니다.".format(send, k))
            # 중복제거 된 신고리스트를 확인하여
            for send_user in report_list:
                # 신고한사람에게 메일을 보낸다
                if send_user.split()[1] == send:
                    report_send[send_user.split()[0]] = report_send[send_user.split()[0]] + 1
   
    print(report_send)

    # 최종값 answer에 입력
    for result in id_list:
        answer.append(report_send[result])
    
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi", "apeach muzi"], 2))
# 순위	당첨 내용
#  1	6개 번호가 모두 일치
#  2	5개 번호가 일치
#  3	4개 번호가 일치
#  4	3개 번호가 일치
#  5	2개 번호가 일치
#  6(낙첨)	그 외
#  최고 당첨순위와 최저 당첨순위 리턴

def solution(lottos, win_nums):
    answer = []

    # 맞춘 갯수 등수출력 사전 생성
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    # 리스트 간 비교를 위해 set 타입으로 변경
    set_lottos = set(lottos)
    set_nums = set(win_nums)
    
    # 로또번호 중 지워진 번호(0) 갯수 확인
    zero_cnt = lottos.count(0)
    # 0제외 맞춘 숫자 세팅
    corr_num = set_lottos & set_nums

    # 0이 6개인경우 1등과 6등
    if zero_cnt == 6:
        answer = [1,6]
    # 모두 맞춘경우 1등
    elif len(corr_num) == 6:
        answer = [1,1]
    # 나머지의 경우, 최소 기댓값은 입력해서 맞춘 등수, 
    # 최대 기댓값은 남은 당첨숫자와 0 갯수를 비교하여
    # 0보다 남은갯수가 많으면 0의 갯수, 적으면 남은 당첨숫자만큼 맞춘 순위 출력
    else:
        rest_win_num = len(set_nums - set_lottos)
        if rest_win_num >= zero_cnt:
            answer = [rank[len(corr_num) + zero_cnt], rank[len(corr_num)]]
        else:
            answer = [rank[len(corr_num) + rest_win_num], rank[len(corr_num)]]

    print(answer)

    return answer



solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])
solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])
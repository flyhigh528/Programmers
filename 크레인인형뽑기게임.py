# board
# [0,0,0,0,0][] [0, 0]
# [0,0,1,0,3][] [1, 0]
# [0,2,5,0,1][] [2, 0]
# [4,2,4,4,2][] [3, 0]
# [3,5,1,3,1][] [4, 0]
# moves
# [1,5,3,5,1,2,1,4]

def solution(board, moves):
    answer = 0
    pop_cnt = 0
    pop_lst = []
    # moves 갯수만큼
    for i in range(len(moves)):
        # board 갯수만큼
        for j in range(len(board)):
            # moves 숫자의 board 값이 0(빈칸)이 아닌경우
            if board[j][moves[i]-1] > 0:
                # print("pop바구니", pop_lst)
                # print("moves값:{}, board[{}][{}]값:{}".format(moves[i], j, moves[i]-1, board[j][moves[i]-1]))
                
                # pop바구니에 인형이 있고, 바로 전 인형이 현재 인형과 같을 때
                if (len(pop_lst) > 0) and (pop_lst[len(pop_lst)-1] == board[j][moves[i]-1]):
                    # 인형 꺼낸자리 비움처리
                    board[j][moves[i]-1] = 0
                    # pop 바구니 같은 인형 꺼내기
                    pop_lst.pop()
                    # 터진 카운트 up
                    pop_cnt += 1
                    break
                else:
                    # pop바구니에 아무것도 없으면 입력처리 후 꺼낸 인형자리 비움처리
                    pop_lst.append(board[j][moves[i]-1])
                    board[j][moves[i]-1] = 0
                    break

    answer = pop_cnt * 2
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))


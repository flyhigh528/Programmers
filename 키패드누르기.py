# 1[0:0] 2[0:1] 3[0:2]
# 4[1:0] 5[1:1] 6[1:2]
# 7[2:0] 8[2:1] 9[2:2]
# *[3:0] 0[3:1] #[3:2]
# 맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작
# 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1
# 1, 4, 7을 입력할 때는 왼손 엄지손가락
# 3, 6, 9를 입력할 때는 오른손 엄지손가락
# 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락
# 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락

def solution(numbers, hand):    
    answer = ''
    key_map = {1:'0:0',   2:'0:1',   3:'0:2', 
               4:'1:0',   5:'1:1',   6:'1:2', 
               7:'2:0',   8:'2:1',   9:'2:2', 
                          0:'3:1'}
    left_now = '3:0'
    right_now = '3:2'

    # 입력순서대로
    for i in numbers:
        # 1, 4, 7, * 일때는 왼쪽 엄지로
        if i in (1, 4, 7, '*'):
            answer += 'L'
            left_now = key_map.get(i)
        # 3, 6 ,9, # 일때는 오른쪽 엄지로
        elif i in (3, 6, 9, '#'):
            answer += 'R'
            right_now = key_map.get(i)
        # 나머지 숫자는 가까운 엄지로        
        else:
            # 숫자와 왼손, 숫자와 오른손의 거리를 좌표로 절대값 거리 계산
            between_r = abs(int(right_now.split(':')[0]) - int(key_map.get(i).split(':')[0])) + abs(int(right_now.split(':')[1]) - int(key_map.get(i).split(':')[1]))
            between_l = abs(int(left_now.split(':')[0]) - int(key_map.get(i).split(':')[0])) + abs(int(left_now.split(':')[1]) - int(key_map.get(i).split(':')[1]))
            # print("오른손 위치 {} 거리 {}, 왼손 위치 {} 거리 {}".format(right_now, between_r, left_now, between_l))
            # 왼손이 가까우면 왼손 엄지
            if between_l < between_r:
                answer += 'L'
                left_now = key_map.get(i)
            # 오른손이 가까우면 오른 엄지
            elif between_r < between_l:
                answer += 'R'
                right_now = key_map.get(i)
            # 거리가 같으면 주사용 손 엄지
            elif between_r == between_l:
                if hand == 'left':
                  answer += 'L'
                  left_now = key_map.get(i)
                elif hand == 'right':
                  answer += 'R'
                  right_now = key_map.get(i)        

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))


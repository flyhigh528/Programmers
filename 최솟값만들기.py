# 입력받은 배열 2개의 곱의 합산값 중 최소값 구하기
# 두 배열의 곱이 가장 적게 하려면 최소값 * 최대값이 가장 합이 적음
# 배열 A의 최소값과 배열 B의 최대값을 순차적으로 곱하기
def solution(A,B):
    answer = 0

    # 정렬을 위한 임시 리스트 생성
    List_A = A
    List_B = B

    # 순차적 최소값, 최대값 선택을 위한 
    # A리스트 오름차순정렬, B리스트 내림차순 정렬
    List_A.sort()
    List_B.sort(reverse=True)

    # print(List_A, List_B)

    # A,B 배열의 0번째부터 리스트길이까지 순차적으로 곱한 후
    # 결과값에 더하기
    for i in range(0, len(List_A)):
        answer += List_A[i] * List_B[i]
    
    print(answer)

    return answer



solution([1, 4, 2], [5, 4, 4])
solution([1, 2], [3, 4])
# 문제 설명
# 124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.

# 124 나라에는 자연수만 존재합니다.
# 124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
# 예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.

# 10진법	124 나라	10진법	124 나라
# 1	1	6	14
# 2	2	7	21
# 3	4	8	22
# 4	11	9	24
# 5	12	10	41
# 자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록 solution 함수를 완성해 주세요.

# 제한사항
# n은 500,000,000이하의 자연수 입니다.
# 입출력 예
# n	result
# 1	1
# 2	2
# 3	4
# 4	11

# 문제풀이
# 기본적인 수식은 진수변환 시 나머지 값을 뒤집는 방식
# 나머지 값이 0일때 몫의 값을 -1, 시켜서 계산
# 나머지의 값이 0인경우는 4로 치환 해준다

def solution(n):
    answer = ''

    print(n, n//3, n%3)

    while n:
        # n%3이 0이면 4로 치환, 몫에서 -1을 해준다
        if n%3 == 0:
            answer += '4'
            n = n//3 -1
        # n%3이 0이 아니면, 나머지 값을 결과 값에 넣은뒤, n값 몫으로 변경
        else:
            answer += str(n%3)
            n = n//3
        
    # 나머지값을 뒤집어서 결과 전달
    return answer[::-1]

print(solution(15))


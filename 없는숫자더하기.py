# 입력받은 배열에서 없는 숫자의 합 리턴
# 너무 쉬워서.. 노코멘트!!!
# easy~~!!!

def solution(numbers):
    answer = 0
    number = {0,1,2,3,4,5,6,7,8,9}
    input_numbers = set(numbers)
    
    num_list = number - input_numbers
    
    for i in num_list:
        answer += i    
    
    return answer


solution([1, 2, 3, 4, 6, 7, 8, 0])
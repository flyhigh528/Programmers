li = ['Korea', 'America', 'China']  # li 초기화
a=0                                                    # a 초기화
str01 = ''                                           # str01 초기화

for i in li:                                           # 바깥쪽 for반복문 수행
   for j in i:                                         # 안쪽 for 반복문 수행
      str01 += j[0]                              # j[0]을 str01에 추가
      a = a + 1                                     # a를 1 증가 시킴

      if a > 5:                                       # a가 5보다 크면
         break                                       # 안쪽 for 반복문을 멈춤 

print('a :', a, ', str01 :', str01)
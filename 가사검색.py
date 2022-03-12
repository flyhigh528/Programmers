# 실패 문자열 검색은 trie 구조를 사용해야한다고함#
# ###########################################################################################
# def solution(words, queries):
#     answer = []
#     q_len = 0
    
#     result = dict()

#     for q in queries:
#         result[q] = 0
#         q_len = len(q)
#         # ?가 앞인경우
#         if q.find('?') == 0:
#             q_locate = 'front'
#         #  ?가 뒤쪽에 붙은경우
#         elif q.find('?') > 0:
#             q_locate = 'back'
        
#         # 찾을 문자열 세팅
#         query = q.replace('?','')

#         # print("찾을 가사:",q, q_len, q_locate, query)

#         # 전체글자수가 같은 단어 중
#         # 앞 혹은 뒤의 ? 갯수를 제외한 문자열이 같은경우 카운트업
#         for word in words:
#             # print("{}가 front인경우 {}, back인경우 {}".format(word, word[-(q_len - len(query)):],word[:-(q_len - len(query))]))
#             if q_len == len(word) and q_locate == 'front' and query == word[(q_len - len(query)):]:
#                 result[q] = result[q] + 1
#             elif q_len == len(word) and q_locate == 'back' and query == word[:-(q_len - len(query))]:
#                 result[q] = result[q] + 1

#     # 결과값 세팅
#     for cnt in result.values():
#         answer.append(cnt)

#     # print(answer)
#     return answer


solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
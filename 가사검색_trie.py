
class Trie:
    def __init__(self):
        self.child = dict()
        self.count = 0
    
    def insert(self, str):
        curr = self
        for ch in str:
            curr.count += 1
            if ch not in curr.child:
                curr.child[ch] = Trie()
            
            curr = curr.child[ch]
        curr.count += 1
    
    def search(self, str):
        curr = self
        for ch in str:
            if ch == '?':
                return curr.count
            if ch not in curr.child:
                return 0
            curr = curr.child[ch]
        return curr.count

def solution(words, queries):
    answer = []
    Root = [Trie() for i in range(10000)]
    RERoot = [Trie() for i in range(10000)]

    for str in words:
        Root[len(str)-1].insert(str)
        RERoot[len(str)-1].insert(str[::-1])
    
    for str in queries:
        if str[0] != '?':
            answer.append(Root[len(str)-1].search(str))
        else:
            answer.append(RERoot[len(str)-1].search(str[::-1]))
    
    print(answer)

    return answer


solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
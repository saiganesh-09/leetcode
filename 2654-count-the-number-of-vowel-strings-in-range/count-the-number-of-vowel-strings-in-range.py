class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        # result=0
        # vowels={'a', 'e', 'i', 'o','u'}
        # for i in range(left,right+1):
        #     word=words[i]
        #     if word[0] in vowels and word[-1] in vowels:
        #         result+=1
        # return result
        vowels={'a', 'e', 'i', 'o','u'}
        return sum(1 for i in range(left,right+1) if words[i][0] in vowels and words[i][-1] in vowels)

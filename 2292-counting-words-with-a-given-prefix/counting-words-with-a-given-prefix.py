class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        # count=0
        # n=len(pref)
        # for word in words:
        #     if word[:n]==pref:
        #         count+=1
        # return count
        return sum(1 for word in words if word.startswith(pref))
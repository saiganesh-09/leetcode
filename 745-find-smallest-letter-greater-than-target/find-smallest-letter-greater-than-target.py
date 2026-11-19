class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        start = 0
        end = len(letters) - 1
        k = '{'

        while start <= end:
            mid = (start + end) // 2

            if letters[mid] > target:
                k = letters[mid]
                end = mid - 1
            else:
                start = mid + 1

        if k == '{':
            return letters[0]

        return k
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sg = "".join(c.lower() for c in s if c.isalnum())
        return sg==sg[::-1]
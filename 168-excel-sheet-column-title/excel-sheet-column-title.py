class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result=''
        while columnNumber>0:
            columnNumber-=1
            r=columnNumber%26
            result=chr(r+65)+result
            columnNumber//=26
        return result
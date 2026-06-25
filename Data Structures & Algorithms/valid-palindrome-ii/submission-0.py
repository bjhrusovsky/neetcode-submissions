class Solution:
    def validPalindrome(self, s: str) -> bool:
        begin, end = 0, len(s) - 1
        
        while begin < end:
            if s[begin] != s[end]:
                skipL = s[begin+1: end + 1]
                skipR = s[begin:end]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            begin += 1
            end -= 1
        return True
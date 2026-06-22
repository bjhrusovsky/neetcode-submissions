class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstWordAscii = [0] * 26
        for letter in s:
            currIdx = ord(letter) - ord('a')
            firstWordAscii[currIdx] += 1
        secondWordAscii = [0] * 26
        for char in t:
            currIdx = ord(char) - ord('a')
            secondWordAscii[currIdx] += 1
        return firstWordAscii == secondWordAscii
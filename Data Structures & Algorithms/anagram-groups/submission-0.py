from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for word in strs:
            currWordAscii = [0] * 26
            for letter in word:
                charIndex = ord(letter) - ord('a')
                currWordAscii[charIndex] += 1
            results[str(currWordAscii)].append(word)
        answer = []
        for value in results.values():
            answer.append(value)
        return answer
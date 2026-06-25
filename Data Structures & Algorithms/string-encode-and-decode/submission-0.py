class Solution:

    def encode(self, strs: List[str]) -> str:
        newString = []
        for items in strs:
            newString.append(items)
            newString.append("9830_*13")
        return "".join(newString)

    def decode(self, s: str) -> List[str]:
        answer = []
        s = s.split("9830_*13")

        for item in s:
            if item != "9830_*13":
                answer.append(item)
        return answer[:-1]

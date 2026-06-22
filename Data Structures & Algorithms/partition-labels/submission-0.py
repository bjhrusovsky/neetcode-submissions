class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # first thing we do is mark last position of char.
        endPoints= {}
        for key, value in enumerate(s):
            endPoints[value] = key
        ans = []
        size, end = 0, 0
        for key, value in enumerate(s):
            size += 1
            end = max(endPoints[value], end)
            if key == end:
                ans.append(size)
                size = 0

        return ans
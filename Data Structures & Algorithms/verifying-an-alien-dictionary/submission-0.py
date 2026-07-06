class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_Dict = {character: index for index, character in enumerate(order)}

        def compare(word):
            return [order_Dict[c] for c in word]
        
        return words == sorted(words, key=compare)
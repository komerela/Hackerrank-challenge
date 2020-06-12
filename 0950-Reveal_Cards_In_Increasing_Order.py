class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        for i in range(len(deck)-2, 0, -1):
            deck.insert(i, deck.pop())
        return deck
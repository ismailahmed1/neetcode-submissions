class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if not len(hand) % groupSize == 0:
            return False
        
        hand_freq = defaultdict(int)

        for i in hand:
            hand_freq[i] += 1
        
        while (sum(hand_freq.values())):
            minimum_val = min(k for k, v in hand_freq.items() if v > 0)            
            for i in range(groupSize):
                if not hand_freq[minimum_val + i]:
                    return False
                else:
                    hand_freq[minimum_val + i] -= 1

        return True
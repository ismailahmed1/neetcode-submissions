class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_elems = defaultdict(int)
        val_list = []

        for i, n in enumerate(nums):
            if n in freq_elems:
                freq_elems[n] += 1
            else:
                freq_elems[n] = 1

        for i in range(0, k):
            max_key = max(freq_elems, key=freq_elems.get)
            val_list.append(max_key)
            freq_elems.pop(max_key)

        return val_list

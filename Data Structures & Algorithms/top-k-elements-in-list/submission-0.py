class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num] += 1
        possible_frequencies = [0]*(len(nums)+1)
        for num, freq in frequencies.items():
            if possible_frequencies[freq] == 0:
                possible_frequencies[freq] = [num]
            else:
                possible_frequencies[freq].append(num)
        answer = []
        for i in range(len(possible_frequencies)-1, -1, -1):
            if k == 0:
                break
            if possible_frequencies[i] != 0:
                answer.extend(possible_frequencies[i])
                k-=len(possible_frequencies[i])
        return answer
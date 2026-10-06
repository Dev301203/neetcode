class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = defaultdict(int)
        for j, i in enumerate(nums):
            remainder = target - i
            if remainder in remaining:
                return [remaining[remainder], j]
            remaining[i] = j
        

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            com = target-nums[i]
            if nums[i] in d:
                return [d[nums[i]], i]
            d[com]=i
        return[]

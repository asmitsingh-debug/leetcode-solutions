class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(0,len(nums)):
            tar=target-nums[i]
            if tar in seen:
                return [seen[tar],i]
            seen[nums[i]]=i
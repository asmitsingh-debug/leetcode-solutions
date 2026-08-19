class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m=max(nums)

        for i in range(len(nums)):
            if nums[i]==m:
                continue
            if nums[i]*2<=m:
                continue
            else:
                return -1
        return nums.index(m)
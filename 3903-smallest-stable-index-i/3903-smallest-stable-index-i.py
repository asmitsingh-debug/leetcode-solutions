class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxi=0
        mini=0
        for i in range(0,len(nums)):
            maxi=max(maxi,nums[i])
            mini=min(nums[i:])
            if maxi-mini<=k:
                return i
        return -1
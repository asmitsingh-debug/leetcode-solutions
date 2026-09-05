class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        arr=[0]*n
        arr[-1]=nums[-1]
        maxi=0
        for i in range(n-2,-1,-1):
            if arr[i+1]>nums[i]:
                arr[i]=nums[i]
            else:
                arr[i]=arr[i+1]
        for i in range(n):
            maxi=max(nums[i],maxi)
            if maxi-arr[i]<=k:
                return i
        return -1
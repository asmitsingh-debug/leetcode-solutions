class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)-1
        ind=-1
        while l<=h:
            mid=l+(h-l)//2
            if nums[mid]>=target:
                ind=mid
                h=mid-1
            else:
                l=mid+1
        if ind!=-1 and nums[ind]==target:
            return ind
        else:
            return l
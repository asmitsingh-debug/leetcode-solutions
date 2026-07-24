class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1
        def lowerbnd(nums,low,high):
            lb=-1
            while low<=high:
                mid=low+(high-low)//2
                if nums[mid]>=target:
                    lb=mid
                    high=mid-1
                else:
                    low=mid+1
            return lb 
        def upperbnd(nums,low,high):
            ub=-1
            while low<=high:
                mid=low+(high-low)//2
                if nums[mid]>target:
                    ub=mid
                    high=mid-1
                else:
                    low=mid+1
            if ub == -1:
                return len(nums) - 1
            return ub - 1
        a=lowerbnd(nums,low,high)
        b=upperbnd(nums,low,high)
        if a == -1 or nums[a] != target:
            return [-1, -1]
        
        return (a,b)
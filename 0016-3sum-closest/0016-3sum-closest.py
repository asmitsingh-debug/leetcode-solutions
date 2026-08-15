class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        i=0
        su=sum(nums[:3])
        while i<len(nums)-2:
            j=i+1
            k=len(nums)-1
            while j<k:
                total=nums[i]+nums[j]+nums[k]
                if abs(total-target)<abs(su-target):
                    su=total
                if total<target:
                    j+=1
                elif total>target:
                    k-=1
                else:
                    return target
            i+=1
        return su
                
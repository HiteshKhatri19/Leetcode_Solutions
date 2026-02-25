class solution(object):
    def twosum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return[]
sol=solution()
print(sol.twosum([2,7,11,15],9))
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
           total = [] 
           for i in range(0, len(nums)): # O(n)
            for j in range(i + 1, len(nums)): # O(n)^2
                if nums[i] + nums[j] == target: # O(1)
                    total.append(i) # 0(1)
                    total.append(j)
                    return total #O(1)
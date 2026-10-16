class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1

        while start < end: #While start does not go past the end of the array 
            mid = (start + end) // 2 #mid = the half the array 

            if nums[mid] > nums[end]: #if num index of mid is greater than num index of end
                start = mid + 1   # start = mid + 1 
            else:
                end = mid       # mid equates to end 

        return nums[start]   
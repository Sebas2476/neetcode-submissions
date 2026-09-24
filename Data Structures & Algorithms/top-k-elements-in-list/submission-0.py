class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            hash = {}
            result_values = []
    
            for num in nums:
                hash[num] = hash.get(num, 0) + 1

            #find a way to sort the hash
            most_used = sorted(hash, key=hash.get, reverse= True)
            for i in range(len(most_used)):
                if (i < k):
                    result_values.append(most_used[i])

            return result_values

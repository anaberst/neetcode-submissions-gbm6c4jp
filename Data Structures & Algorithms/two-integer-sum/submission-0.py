class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        prev_vals = {}

        for i in range(len(nums)):
            current = nums[i]
            diff = target - current

            if diff in prev_vals:
                return [prev_vals[diff], i]
            
            else:
                prev_vals[current] = i

class Solution:        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = []
        for i in range (len(nums) - 1):
            for j in range (i, len(nums)):
                if (nums[i] + nums [j]) == target:
                    sol.append(i)
                    sol.append(j)
                    return sol

target = 9
nums = [2, 7, 11, 15]
res = []
a = Solution()
print(a.twoSum(nums, target))

class Solution:   
    def getPerms(self, nums, idx, ans):
        if idx == len(nums):
            ans.append(nums.copy())
            return
        
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]   # swap
            self.getPerms(nums, idx + 1, ans)
            nums[idx], nums[i] = nums[i], nums[idx]   # backtrack

    def permute(self, nums):
        ans = []
        self.getPerms(nums, 0, ans)
        return ans

# Main program
obj = Solution()
nums = [1, 2, 3]
result = obj.permute(nums)
print("Permutations are:")
for p in result:
    print(p)
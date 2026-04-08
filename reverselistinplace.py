#using two pointers
def reverse_inplace(nums):
    left=0
    right=len(nums)-1

    while left<right:
        #swap nums left and right
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1

nums=[5,7,3,2,8]
print("before:",nums)
reverse_inplace(nums)
print("After:",nums)
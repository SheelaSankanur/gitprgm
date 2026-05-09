def process_num(nums):
    evens=[x for x in nums if x%2==0]
    reversed_evens=evens[::-1]
    return reversed_evens,len(evens)
nums=[1,2,3,4,5,6,7,8]
reversed_evens, count = process_num(nums)
print(f"Reversed evens: {reversed_evens}, Count of evens: {count}") 
print("count of evens:", count)
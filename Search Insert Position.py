def searchInsert(nums,target):
    for i in range(len(nums)):
        if nums[i]==target:
            print(i)
            break
        elif nums[i]>target:
            print(i-1)
            break
        elif nums[i]+1==target:
            print(i+1)
            break
searchInsert([1,3,5,6],5)
searchInsert([1,3,5,6],2)
searchInsert([1,3,5,6],7)

    
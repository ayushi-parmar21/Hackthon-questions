def searchRange(nums,target):
    list=[]
    if target in nums:
        for i in range(len(nums)):
            if nums[i]==target:
                list.append(i)
        list2=[]
        list2.append(list[0])
        list2.append(list[-1])
        print(list2)
    else:
        print([-1,-1])
searchRange([5,7,7,8,8,8],8)
searchRange([5,7,7,8,8,10],6)
searchRange([],6)
def removeDuplicates(nums):
    list=[]
    count=0
    for i in range(len(nums)):
        if nums[i] not in list:
            list.append(nums[i])
        else:
            count+=1
    for i in range(1,count+1):
        ayu=["_"]
        list.extend(ayu)
    print(list)
removeDuplicates([1,1,2])
removeDuplicates([0,0,1,1,1,2,2,3,3,4])

def deleteDuplicates(nums):
    list=[]
    for i in range(len(nums)):
        count=0
        for j in range(len(nums)):
            if nums[i]==nums[j]:
                count+=1
        if count==1:
            list.append(nums[i])
    print(list)
deleteDuplicates([1,2,3,3,4,4,5])
deleteDuplicates([1,1,1,2,3])
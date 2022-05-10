def mergeKLists(nums):
    if nums==[[],[]] or nums==[[]] or nums==[]:
        print([])
    else:
        list=[]
        for i in range(len(nums)):
            for j  in range(len(nums[i])):
                num=nums[i][j]
                list.append(num)
        list.sort()
        print(list) 
mergeKLists([[1,4,5],[1,3,4],[2,6]])
mergeKLists([[]])
mergeKLists([[],[]])
    
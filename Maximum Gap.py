def maximumGap(nums):
    if len(nums)<=2:
        print(0)
    else:
        first=0
        last=0
        min1=0
        for i in range(len(nums)):
            first=nums[i]
            min=first-last
            if min>=min1:
                min1=min
            last=nums[i]
        print(min1)
maximumGap([3,6,9,1])
maximumGap([10])
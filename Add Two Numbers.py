def plusOne(nums,nums1):
    plus,plus1=0,0
    nums.reverse()
    nums1.reverse()
    for i in range(len(nums)):
        plus=plus*10+nums[i]
    for j in range(len(nums1)):
        plus1=plus1*10+nums1[j]
    sum=plus+plus1
    digits = [int(x) for x in str(sum)]
    digits.reverse()
    print(digits)
plusOne([2,4,3],[5,6,4])
plusOne([9,9,9,9,9,9,9],[9,9,9,9])
plusOne([0],[0])
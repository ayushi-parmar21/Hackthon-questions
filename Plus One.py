import string


def plusOne(nums):
    plus=0
    for i in range(len(nums)):
        plus=plus*10+nums[i]
    plus=plus+1
    digits = [int(x) for x in str(plus)]
    print(digits)
plusOne([1,2,3])
plusOne([4,3,2,1])
plusOne([9])

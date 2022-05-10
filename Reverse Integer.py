def reverse(nums):
    plus=0
    if nums<0:
        nums*=-1
        digits = [int(x) for x in str(nums)]
        digits.reverse()
        for i in range(len(digits)):
            plus=plus*10+digits[i]
        print(-plus)
    else:
        digits = [int(x) for x in str(nums)]
        digits.reverse()
        for i in range(len(digits)):
            plus=plus*10+digits[i]
        print(plus)
reverse(123)
reverse(-123)
reverse(120)

    
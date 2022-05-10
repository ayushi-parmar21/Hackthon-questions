def countDigitOne(nums):
    count=0
    for i in range(0,nums+1):
        if i<=9:
            if i==1:
                count+=1
        else:
            j=i
            while j!=0:
                r=j%10
                j//=10
                if r==1:
                    count+=1
                i+=1
    print(count)
countDigitOne(13)
countDigitOne(0)

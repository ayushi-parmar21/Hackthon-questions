def count(nums):
    counts=0
    for j in range(1,nums+1):
        count= 0
        i = 2
        while i <= j / 2:
            if j % i == 0:
                count+=1
                break
            i=i+1
        if j==1:
            pass
        elif count==0:
            counts+=1
    print(counts)
count(10)
count(0)
count(1)
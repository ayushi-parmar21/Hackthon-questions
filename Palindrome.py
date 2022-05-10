def isPalindrome(nums):
    temp=nums
    rev=0
    while(nums>0):
        dig=nums%10
        rev=rev*10+dig
        nums=nums//10
    if(temp==rev):
        print("True")
    else:
        print("False")
isPalindrome(int(input("Enter number:")))
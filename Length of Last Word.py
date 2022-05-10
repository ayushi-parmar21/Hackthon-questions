def lengthOfLastWord(nums):
    S=nums.split()
    count=0
    for i in range(len(S[-1])):
        count+=1
    print(count)
lengthOfLastWord("Hello World")
lengthOfLastWord("   fly me   to   the moon  ")
lengthOfLastWord("luffy is still joyboy")
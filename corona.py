# Every decimal number can be changed into its binary form. Suppose your computer has it’s own CoronaVirus, that eats binary digits from the right side of a number. Suppose a virus has 6 spikes, it will eat up 6 LSB binary digits in your numbers.
# You will have a bunch of numbers, and your machine will have a virus with n spikes, you have to calculate what will be the final situation of the final numbers.
# Input Format:
# First line, a single Integer N
# Second line N space separated integers of the bunch of values as array V
# Third line a single integer n, the number of spikes in Corona for Computer
# Output Format:
# Single N space separated integers denoting the final situation with the array v.
# Sample Input:
# 5
# 1 2 3 4 5
# 2
# Output:
# 0 0 0 1 1

n=int(input("Enter limit:"))
l=list(map(int,input().split()))
bi=[]
for i in l:
    bi.append(bin(i)[2:])
spike=int(input("Enter the spikes:"))
res=[]
for i in bi:
    if len(i)<=spike:
        res.append(0)
    else:
        num=i[:-spike]
        res.append(int(num,2))
print(*res)

# for i in l:
#     if i >> spike == 0:
#         res.append(0)
#     else:
#         res.append(i >> spike)

# print(*res)
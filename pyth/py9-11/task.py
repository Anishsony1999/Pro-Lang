
a = ['flight','flower','flag']
# a = ['ddog','ddam','ddd']
# a=['cricket','football','hockey']

# def lonPrefix(a):
#     ans =""
#     for i in range(len(a)):
#         for j in range(i+1,len(a)):
#             if a[0][i] == a[j][i]:
#                 ans += a[i][i]
#             else:
#                 return ans
#     return ans

# print(lonPrefix(a))


# def longestCommonPrefix(strs):
#     if not strs:
#         return ""
#     shortest = min(strs, key=len)
#     for i, ch in enumerate(shortest):
#         for other in strs:
#             if other[i] != ch:
#                 return shortest[:i]
#     return shortest

# print(longestCommonPrefix(a))

def longestCommonPrefix(list1):
    list1.sort()
    x= list1[0]
    y= list1[-1]

    ans = ""

    for i in range(min(len(x),len(y))):
        if x[i] != y[i]:
            return ans
        ans += x[i]

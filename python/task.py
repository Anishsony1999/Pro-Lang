# 567 -> 765
# -21 -> -12


num = 567 # 0
ans = 0 # 765

while num > 0 :

    n = num % 10
    num = num // 10  # 56.7 -> 56
    ans  = ans * 10 + n

print(ans)


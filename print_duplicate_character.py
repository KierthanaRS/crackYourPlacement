from collections import Counter
s=input()
d=Counter(s)
for i in d:
    if d[i]>1:
        print(i," occurs ",d[i])
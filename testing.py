from collections import Counter
import math
s = 'abcbaba'
res = [s[i:j] for i in range(len(s)) for j in range(len(s)+1)]
nres = []
subs = []
for i in res:
    if i != '':
        nres.append(i)
for su in nres:
    if len(su) == 1:
        subs.append(su)
    else:
        flag = True
        for j in range(0,len(su)-1):
            if su[j] != su[j+1]:
                flag = False
                break
        if flag == True:
            subs.append(su)
        else:
            flag = True
            if (len(su))%2 == 1:
                m = math.floor(len(su)/2)
                li = list(su)
                li.remove(li[m]) 
                for j in range(0,len(li)-1):
                    if li[j] != li[j+1]:
                        flag = False
                        break
                if flag == True:
                    subs.append(su)
print(subs)
print(len(subs))
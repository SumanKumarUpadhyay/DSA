# find repeating word in string
s = "Suman Kumar"
count={}
for i in range(len(s)):
    if s[i] in count:
        count[s[i]] +=1
    else:
        count[s[i]] = 1
print(count)
for it in count:
    if count[it]>1:
        print(it,"count",count[it])

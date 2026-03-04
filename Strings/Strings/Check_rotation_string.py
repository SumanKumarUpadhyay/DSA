# check rotated string
s1 = "ABCD"
s2 = "ACBD"
if len(s1)!=len(s2):
    print("not rotated")
temp=s1+s1
if s2 in temp:
    print("yes s2 is rotation of s1")
else:
    print("not s2 is rotation")
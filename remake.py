a = []
s = input()
while s != "end":
    s = s.replace(" ","")
    a.append(s)
    s = input()

b = [i for i in a[0::4]]
c = [i for i in a[1::4]]
d = [i for i in a[2::4]]
e = [i for i in a[3::4]]

print(b)
print(c)
print(d)
print(e)
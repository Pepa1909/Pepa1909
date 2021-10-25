a=3
b=7
c=-1

#var 1
if a<b and a<c:
    m=a
elif b<a and a<c:
    m=b
elif c<a and c<b:
    m=c
print(m)

#var 2
if a<b and a<c:
    m=a
elif b<c:
    m=b
else:
    m=c
print(m)

#var 3
if a<b:
    m=a
else:
    m=b
if c<m:
    m=c
print(m)
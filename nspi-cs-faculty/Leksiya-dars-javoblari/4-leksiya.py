# 1-topshiriq
n=int(input('n='))
r = []
for i in range(1,n+1):
  s=0
  for j in range(1,i+1):
    s += j
  r.append(i)
  r.append(s)
print(r)

d = {i:(1+i)/2*i for i in range(1,n+1)}
print(d)

# 2-topshiriq
n = int(input('n='))
r = []
for i in range(1,n+1):
  r.append(i)
print(r)
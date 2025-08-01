arr=[1,0,2,2,2,2,0,0,1,1,0,0,1,0,2,1,0]
a = arr.count(0)
b = arr.count(1)
c = arr.count(2)

r = [0]*a+[1]*b+[2]*c
print(r)
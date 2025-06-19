n1=int(input("Enter a number: "))
n2=int(input("Enter another number:"))

a=set()
b=set()
for i in range(1,n1+1):
    if n1%i==0:
        a.add(i)

for i in range(1,n2+1):
    if n2%i==0:
        b.add(i)


gcd=max(a.intersection(b))
print(f"The GCD of {n1} and {n2} is: {gcd}")
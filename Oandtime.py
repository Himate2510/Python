def OnTime(n):
    iteration=0
    for i in range(1,n+1):
        iteration+=1
    print("N is ", n," iterations = ", iteration)

OnTime(10)
OnTime(15)
OnTime(20)

print("\n With every n taken the iterations shall increase")
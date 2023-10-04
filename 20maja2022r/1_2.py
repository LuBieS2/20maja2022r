A=[1, 3, 1]
n=len(A)
wy=[]
for i in A:
     if i>n:
         wy.append(i)
     elif i<=0:
         wy.append(i)
     elif i not in wy:
        for l in range(A.count(i)-1):
             wy.append(i)
     print(wy)

def prime(a):
    if a==1 or a<1:
        return False
    else:
        m=0
        if a==2:
            return True
        for x in range(2, a-1):
            #print(x)
            if a%x!=0:
                pass
            else:
                m=m+1
        if m>0:
            return False
        else:
            return True

file=open("orzyklad.txt", "r")
numbers= list(map(str.strip, file.readlines()))

#4.1
digits=[]
temp_counter=[]
for i in numbers:
    for x in i:
        temp_counter.append(x)
    digits.append(temp_counter)
    temp_counter=[]
digits_last_and_first=[]
for i in digits:
    if i[0] == i[-1]:
        digits_last_and_first.append("".join(i))
#print(digits_last_and_first)
#print(len(digits_last_and_first))
#4.2
primen=[]
highest_primes=0
n_hp=""
h_pu=0
n_hpu=""
for i in numbers:
    print(i)
    c=i
    while int(i)>1:
        
        for x in range(1, int(i)+1):
            b=x
            if int(i)%x==0:
                if prime(x)==True:
                    primen.append(x)
                    i=float(i)/b
    if len(primen)>highest_primes:
        highest_primes=len(primen)
        n_hp=c
    primenu=set(primen)
    
    if len(primenu)>int(h_pu):
      h_pu=len(primenu)
      n_hpu=c
    print(primen)
    primen=[]        
print(highest_primes, n_hp)
print(h_pu, n_hpu)
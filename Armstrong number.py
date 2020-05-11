number=int(input())
sum=0
r= list(map(int, str(number)))
print(r)
for i in r:
    n=i**3
    sum+=n

if (sum==number):
    print("It is armstrong number")
else:
    print("It is not armstrong number")

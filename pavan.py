for i in range(1,9):
    if(i%3 !=0 and i%5 !=0):
        print(i)

for i in range(1,11):
    if(i%3 ==0 or i%5==0):
        continue
    print(i)

for i in range(5):
    if(i==3):
        continue
    print(i)

x = int(input("how many candies do you want"))
i =1
av =5
while i <= x:
    if i > av:
        print("out of stock")
        break
    print("candy")
    i = i+1

print("bye")
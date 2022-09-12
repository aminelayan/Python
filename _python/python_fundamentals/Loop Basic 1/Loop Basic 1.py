# Basic
for x in range(0,150):
    print(x)
# Multiples of Five
for z in range(0,1000,5):
    print(z)
# Counting, the Dojo Way
for a in range(0,100):
    if (a%10==0):
        print("Coding Dojo")
    elif(a%5==0):
        print("Coding")
    else: print(a)
#Whoa. That Sucker's Huge
sum=0
for x in range(0,500000):
    if x % 2 != 0:
        sum += x
        
 print(sum)
# Countdown by Fours
for o in range(2018,0,-4):
    print(o)
#Flexible Counter
lownum=2
highnum=9
mult=3

for a in range(lownum,highnum+1):
    if a%mult==0:
        print(a)

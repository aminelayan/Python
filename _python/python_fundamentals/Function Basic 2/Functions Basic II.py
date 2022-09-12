#1 Countdown
def countdown(a):
    result = []
    for x in range(a, 0, -1):
        result.append(x)
    return result
print(countdown(5))

#2.Print and Return
def printandreturn(i,j):
    print(i)
    return j
print(printandreturn(1,2))

#3 First Plus Length
def firstlen(list):
    sum=list[0]+len(list)
    return sum
list=[1,2,3,4,5]
print(firstlen(list))

#4 Values Greater than Second
def greaterthan(list):
    maxlist=[]
    if(len(list)<2):
        return False
    max=list[1]
    for x in range(0,len(list)):
        if(list[x]>max):
            maxlist.append(list[x])
    return maxlist
print(greaterthan([1,2,3,4,5,2]))
print(greaterthan([3]))

#5 This Length, That Value
def lengthvalue(s,v):
    list=[]
    for x in range(0,s):
        list.append(v)
    return list
print(lengthvalue(6,9))


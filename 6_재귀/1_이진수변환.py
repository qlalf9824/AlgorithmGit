def binaryChange(num):

    renum = num / 2
    re = num % 2  

    if(num == 1):
        return "1"
    elif(num < 1):
        return ""
    
    return  binaryChange(renum) + str(int(re))

n = int(input())

print(binaryChange(n))
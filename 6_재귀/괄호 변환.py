def solution(p):

    if(p == ""):
        return ""
    
    u = ""
    c = 0
    flag = 0

    for i in p:
        u += i
        
        if(i == "("):
            c += 1
        elif(i == ")"):
            if(c==0):
                flag = 1
            else:
                c -= 1

        if(u.count("(") == u.count(")")):
            break
    
    v = p[len(u):]
    print("u", u)
    print("v", v)

    if(flag == 1):
        s = "("
        s += solution(v)
        s += ")"
        s += u[1:len(u)-1].replace("(","/").replace(")","(").replace("/",")")
        return s
    else:
        return u + solution(v)

print(solution("()))((()"))
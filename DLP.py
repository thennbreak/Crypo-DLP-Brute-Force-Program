def bruteLog(e, x, m): #where e is = base, x = unknown, and m = the mod
    k = 1
    for i in range(m):
        k = (k * e) % m
        if k == x:
            return i + 1
    return -1 #if no value exists

ans = bruteLog(106, 12375, 24691)#e, x, m

print("The answer is: " +str(ans))


#*************IMPORTANT************

#ANS: 22392

#*************IMPORTANT************

def power(base,exp):    #exp=exponent
    if exp ==0:
        return 1
    return base *power(base,exp-1)

print(power(3,2)) 
     
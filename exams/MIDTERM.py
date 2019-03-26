def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''    
    result = 0
    if base > num:
        result = 0
    elif base == num:
        result = 1
    else:
        i = 0
        while i < num:
            i += 1
            if abs(base**i - num) <= abs(base**(i + 1) - num):
                result = i
                break
    return result
    
    ##########################################################################
    
    
    def getSublists(L, n):
    newone = []
    for i in range(len(L)):
        if len(L[i:n+i]) < n:
            break
        else:
            newone.append(L[i:n+i])
            i += 1
    return newone
    
    #########################################################################

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    tlist = []
    for i,j in aDict.items():
        if j == target:
            tlist.append(i)
    return sorted(tlist)
    
    
    ###########################################################################
    
    def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)
        
    ##############################################################################
    
    def satisfiesF(L):
    LT = []
    for i in L:
        if f(i) == True:
            LT.append(i)
    L[:] = LT
    return len(L)
    
run_satisfiesF(L, satisfiesF)

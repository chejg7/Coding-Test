import math

def solution(numer1, denom1, numer2, denom2):
    # lcm = math.lcm(denom1, denom2)
    # numer3 = numer1 * (lcm // denom1) + numer2 * (lcm // denom2)
    # denom3 = lcm
    # gcd = math.gcd(numer3, lcm)
    
    numer3 = numer1 * denom2 + numer2 * denom1
    denom3 = denom1 * denom2
    gcd = math.gcd(numer3, denom3)
        
    return [numer3 // gcd, denom3 // gcd]
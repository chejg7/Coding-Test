# import math

# def solution(numer1, denom1, numer2, denom2):
#     # lcm = math.lcm(denom1, denom2)
#     # numer3 = numer1 * (lcm // denom1) + numer2 * (lcm // denom2)
#     # denom3 = lcm
#     # gcd = math.gcd(numer3, lcm)
    
#     numer3 = numer1 * denom2 + numer2 * denom1
#     denom3 = denom1 * denom2
#     gcd = math.gcd(numer3, denom3)
        
#     return [numer3 // gcd, denom3 // gcd]

# 최소공배수는 math 모듈에 없어서 최대공약수만 모듈을 사용해서 구함
# 다른 풀이 중 최대공약수를 아래와 같이 구하는 방식도 있어서 참고함

def solution(denum1, num1, denum2, num2):
    answer = []
    s = 0

    denum0 = (denum1*num2) +(denum2*num1)
    num0 = num1*num2

    for i in range(min(denum0,num0),0,-1):
        if denum0%i == 0 and num0%i == 0:
            s = i
            break

    denum0 /= s
    num0 /= s
    answer.append(denum0)
    answer.append(num0)

    return answer
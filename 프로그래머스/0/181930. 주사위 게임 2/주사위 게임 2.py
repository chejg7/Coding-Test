# def solution(a, b, c):
    # n1, n2, n3 = sorted([a, b, c])
    # if n1 == n2 and n2 == n3:
    #     answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
    # elif (n1 == n2 and n2 != n3) or (n1 != n2 and n2 == n3):
    #     answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    # else:
    #     answer = a + b + c
    # return answer

    # set을 활용해서 동일값만 남길 수 있음
    
def solution(a, b, c):
    check=len(set([a,b,c]))
    if check==1:
        return 3*a*3*(a**2)*3*(a**3)
    elif check==2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return (a+b+c)
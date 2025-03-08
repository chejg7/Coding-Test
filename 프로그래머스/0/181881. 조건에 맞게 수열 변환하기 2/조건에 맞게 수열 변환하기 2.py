def solution(arr):
    answer = 0
    
    def get_new_arr(arr):
        new_arr = []
        for a in arr:
            if a >= 50 and a % 2 == 0:
                new_arr.append(a / 2)
            elif a < 50 and a % 2 == 1:
                new_arr.append(a * 2 + 1)
            else:
                new_arr.append(a)
        return new_arr
    
    while True:
        new_arr = get_new_arr(arr)
        if arr == new_arr:
            break
        else:
            arr = new_arr
            answer += 1
    
    return answer
def solution(n, w, num):
    answer = 0
    x, y = 1, 1
    num_x, num_y = 0, 0
    
    for i in range(1, n + 1):
        if i == num:
            num_x, num_y = x, y
        if x == num_x and y != num_y:
            answer += 1
            
        if i % w == 0:
            y += 1
        else:
            if (i // w) % 2 == 0:
                x += 1
            else:
                x -= 1
                
    return answer + 1
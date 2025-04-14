def solution(keyinput, board):
    answer = [0, 0]
    key_num = {"up": [0, 1], "down": [0, -1], "left": [-1, 0], "right": [1, 0]}
    max_x = board[0] // 2
    max_y = board[1] // 2
    
    for k in keyinput:
        dx, dy = key_num[k]
        new_x = answer[0] + dx
        new_y = answer[1] + dy
        
        if -max_x <= new_x <= max_x and -max_y <= new_y <= max_y:
            answer[0] = new_x
            answer[1] = new_y
        
    return answer
def solution(video_len, pos, op_start, op_end, commands):
    
    # 분과 초로 나누어 조건을 확인하려하면 계산과 비교가 쉽지 않음. 단일 단위인 초만 사용하도록 변경함.
    
    # def make_num_list(time):
    #     return list(map(int, time.split(":")))
    def time_to_sec(time):
        mm, ss = map(int, time.split(":"))
        return mm * 60 + ss
    
    # def make_answer(num_list):
    #     mm, ss = map(str, num_list)
    #     if len(mm) == 1:
    #         mm = "0" + mm
    #     if len(ss) == 1:
    #         ss = "0" + ss
    #     return mm + ":" + ss
    
    def make_answer(sec):
        mm = str(sec // 60)
        ss = str(sec % 60)
        if len(mm) == 1: mm = "0" + mm
        if len(ss) == 1: ss = "0" + ss
        return mm + ":" + ss
        
    # def get_after(time1, time2):
    #     if time1[0] > time2[0]:
    #         return time1
    #     elif time1[0] < time2[0]:
    #         return time2
    #     elif time1[1] > time2[1]:
    #         return time1
    #     else:
    #         return time2
        
    # video_len = make_num_list(video_len)
    # pos = make_num_list(pos)
    # op_start = make_num_list(op_start)
    # op_end = make_num_list(op_end)
    video_len = time_to_sec(video_len)
    pos = time_to_sec(pos)
    op_start = time_to_sec(op_start)
    op_end = time_to_sec(op_end)
    
    # if get_after(op_start, pos) == pos and get_after(pos, op_end) == op_end:
    #     pos = op_end
    if op_start <= pos <= op_end: pos = op_end
            
    for cmd in commands:
                
        if cmd == "next":
            # pos[0] += (pos[1] + 10) // 60
            # pos[1] = (pos[1] + 10) % 60
            # if get_after(video_len, pos) == pos:
            #     pos = video_len
            pos += 10
            if pos > video_len: pos = video_len
                
        if cmd == "prev":
            # pos[1] -= 10            
            # if pos[1] < 0:
            #     pos[0] -= 1
            #     pos[1] += 60
            # if pos[0] < 0:
            #     pos = [0, 0]
            pos -= 10
            if pos < 0: pos = 0
                
        # if get_after(op_start, pos) == pos and get_after(pos, op_end) == op_end:
        #         pos = op_end
        if op_start <= pos <= op_end: pos = op_end
                
    return make_answer(pos)
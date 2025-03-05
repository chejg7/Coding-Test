def solution(data, ext, val_ext, sort_by):
    
    e = 0 if ext == "code" else 1 if ext == "date" else 2 if ext == "maximum" else 3
    s = 0 if sort_by == "code" else 1 if sort_by == "date" else 2 if sort_by == "maximum" else 3
    
    answer = [d for d in data if d[e] < val_ext]
    answer.sort(key = lambda x : x[s])
        
    return answer
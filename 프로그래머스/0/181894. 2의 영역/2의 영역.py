def solution(arr):
    answer = []
    all_idx = [i for i, a in enumerate(arr) if a == 2]
    answer = [-1] if not all_idx else arr[all_idx[0]:all_idx[-1] + 1]
            
    return answer
def solution(todo_list, finished):
    answer = [todo for i, todo in enumerate(todo_list) if not finished[i]]
    return answer
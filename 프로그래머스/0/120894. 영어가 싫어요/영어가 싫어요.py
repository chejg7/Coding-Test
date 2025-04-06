def solution(numbers):
    num_str = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    answer = ""
    temp = ""
    for n in numbers:
        temp += n
        if temp in num_str:
            answer += str(num_str.index(temp))
            temp = ""
        
    return int(answer)
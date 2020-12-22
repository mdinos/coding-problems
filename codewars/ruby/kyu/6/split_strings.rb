# https://www.codewars.com/kata/515de9ae9dcfc28eb6000001

def solution(str)
    arr = []
    i = 0
    while i < str.length do
        if str[i+1] != nil
            arr.push(str[i] + str[i + 1])
        else
            arr.push(str[i] + "_")
        end
        i += 2
    end
    arr
end
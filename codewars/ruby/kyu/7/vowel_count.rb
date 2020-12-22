# https://www.codewars.com/kata/54ff3102c1bad923760001f3

def getCount(inputStr)
    vowels = ['a','e','i','o','u']
    count = 0
    i = 0
    while i < inputStr.length do
      if vowels.include? inputStr[i]
        count += 1
      end
      i += 1
    end
    return count
  end
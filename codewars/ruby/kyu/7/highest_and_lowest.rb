# https://www.codewars.com/kata/554b4ac871d6813a03000035

def high_and_low(numbers)
    numbersArr = numbers.split(' ')
    numbersArr.map! { |i| i.to_i }
    maxVal = numbersArr.max.to_s
    minVal = numbersArr.min.to_s
    return ("#{maxVal} #{minVal}")
  end
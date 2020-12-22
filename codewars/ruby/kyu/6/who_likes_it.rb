# https://www.codewars.com/kata/5266876b8f4bf2da9b000362

def likes(names)
    returnString = ""
    case
    when names.length == 1
      returnString = names[0] + " likes this"
    when names.length == 2 
      returnString = names[0] + " and " + names[1] + " like this"
    when names.length == 3 
      returnString = names[0] + ", " + names[1] + " and " + names[2] + " like this"
    when names.length >= 4
      returnString = names[0] + ", " + names[1] + " and " + (names.length - 2).to_s + " others like this"
    else 
      returnString = "no one likes this"
    end
    returnString
  end
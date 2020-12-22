# https://www.codewars.com/kata/56747fd5cb988479af000028

def get_middle(s)
    len = s.length
    returnstr = ""
    if len % 2 == 0
      returnstr = s[(len / 2) - 1] + s[len / 2]
    elsif len % 2 == 1
      returnstr = s[len / 2]
    end
    return returnstr
  end
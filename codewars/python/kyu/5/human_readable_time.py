# https://www.codewars.com/kata/52685f7382004e774f0001f7

def make_readable(seconds):
    final_secs = seconds % 60
    interrim_mins = ((seconds - final_secs) // 60)
    final_mins = interrim_mins % 60
    final_hrs = (interrim_mins - final_mins) // 60
    return("{0:0=2d}:{1:0=2d}:{2:0=2d}".format(final_hrs, final_mins, final_secs))
class Phone(object):
    def __init__(self, phone_number):
        self.number = self.filter_number(phone_number)
        self.area_code = self.number[0:3]
    
    def pretty(self):
        return '({}) {}-{}'.format(
            self.area_code, 
            self.number[3:6], 
            self.number[6:10])

    def filter_number(self, phone_number):
        number = ''
        for char in phone_number:
            try:
                int(char)
                number += char
            except:
                continue
        if len(number) == 11 and number[0] == '1':
            number = number[1:len(number)]
        elif len(number) != 10:
            raise ValueError("Invalid quantity of numbers.")
        if number[0] in ['0','1'] or number[3] in ['0','1']:
            raise ValueError("Invalid exchange code or area code.")
        return number
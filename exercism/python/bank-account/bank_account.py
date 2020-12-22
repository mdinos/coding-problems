import threading

class BankAccount(object):
    def __init__(self):
        self.openStatus = False
        self.balance = 0
        self.lock = threading.Lock()

    def require_open(func):
        def wrapper(self, *args):
            if not self.openStatus:
                raise ValueError('Cannot get balance of closed account')  
            return func(self, *args)
        return wrapper

    @require_open
    def get_balance(self) -> int:      
        return self.balance

    def open(self) -> None:
        if self.openStatus:
            raise ValueError('Cannot open open bank account')
        self.openStatus = True

    @require_open
    def deposit(self, amount: int) -> None:
        if type(amount) != int or amount < 0:
            raise ValueError('You can only deposit positive integers.')
        self.lock.acquire()
        self.balance += amount
        self.lock.release()

    @require_open
    def withdraw(self, amount: int) -> None:
        if type(amount) != int or amount < 0 or amount > self.balance:
            raise ValueError('You must have funds to cover the amount to withdraw, and to pass a positive integer')
        self.lock.acquire()
        self.balance -= amount
        self.lock.release()

    @require_open
    def close(self) -> None:
        self.balance = 0
        self.openStatus = False
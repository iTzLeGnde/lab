from account import *

class Test:
    def setup_method(self):
        self.a1 = Account("Yasir")
        self.a2 = Account("Abdul")
    def teardown_method(self):
        del self.a1
        del self.a2
    def test_init(self):
        assert self.a1.get_name() == "Yasir"
        assert self.a1.get_balance() == 0
        assert self.a2.get_name() == "Abdul"
        assert self.a2.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(40) == True
        assert self.a1.deposit(0) == False
        assert self.a1.deposit(-5) == False
        assert self.a1.deposit(40.0) == True
        assert self.a1.deposit(0.0) == False
        assert self.a1.deposit(-5.0) == False
    def test_withdraw(self):
        self.a1.deposit(50)
        assert self.a1.withdraw(40) == True
        self.a1.deposit(40)
        assert self.a1.withdraw(51) == False
        assert self.a1.withdraw(50) == True
        assert self.a1.withdraw(0) == False

    def test_get_balance(self):
        self.a1.deposit(50)
        self.a2.deposit(20)
        assert self.a1.get_balance() == 50
        assert self.a2.get_balance() == 20






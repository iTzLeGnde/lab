class Account:
    def __init__(self,name: str):
        '''
        Constructor to create initial state of an account object.
        :param name: The account name
        '''
        self.__account_name = name
        self.__account_balance: float = 0

    def deposit(self, amount: float) -> bool:
        '''
        Function to deposit specifc amount to account_balance
        :param amount: The specific amount
        :return: True if amount deposited successfuly, otherwise False.
        '''
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False
    def withdraw(self,amount: float) -> bool:
        '''
        Function to withdarw specifc amount from account_balance
        :param amount: The specific amount
        :return: True if amount withdrawn successfuly, otherwise False.
        '''
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False
    def get_balance(self) -> float:
        '''
        Function to get the balance from account_balance
        :return: the balance
        '''
        return self.__account_balance

    def get_name(self) -> str:
        '''
        Function to get the name from account_name
        :return: the name
        '''
        return self.__account_name

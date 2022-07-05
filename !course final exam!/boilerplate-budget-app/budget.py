class Category:
    ledger = list()
    balance = 0

    def __init__(self, category):
        self.category = category

    def deposit(self, amount, *description):
        if isinstance(description,tuple):
            if len(description) == 1:
                description = description[0]
            else:
                description = ""
        #The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
        self.ledger.insert(0,{"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, *description):
        if isinstance(description, tuple):
            if len(description) == 1:
                description = description[0]
            else:
                description = ""
        #This method should return True if the withdrawal took place, and False otherwise.
        if self.balance >= amount:
            self.ledger.insert(0, {"amount": -amount, "description": description})
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        #returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
        return self.balance

    def get_transfer(self, amount, from_category):
        self.ledger.insert(0, {"amount": amount, "Transfer from":  from_category})
        self.balance += amount

    def transfer(self, amount,target_category):
        """A transfer method that accepts an amount and another budget category as arguments.
         The method should add a withdrawal with the amount and the description
         "Transfer to [Destination Budget Category]". The method should then add a deposit to the other
         budget category with the amount and the description "Transfer from [Source Budget Category]".
          If there are not enough funds, nothing should be added to either ledgers."""
        if self.balance >= amount:
            self.ledger.insert(0, {"amount": -amount, "Transfer to":  target_category})
            target_category.get_transfer(amount, self.category)
            self.balance -= amount
            # This method should return True if the transfer took place, and False otherwise.
            return True
        else:
            return False

    def check_funds(self, amount):
        """
        A check_funds method that accepts an amount as an argument. This method should be used by both the withdraw
        method and transfer method.
        """
        # It returns False if the amount is greater than the balance of the budget category and
        #returns True otherwise.
        if amount <= self.balance:
            return True
        else:
            return False

    def __str__(self):
        # title creation
        star_count = (30 - len(self.category)) // 2
        title = ""
        #make stars before
        for i in range(star_count):
            title += "*"
        #adding name
        title += self.category
        #make stars after
        star_count = 30 - len(title)
        for i in range(star_count):
            title += "*"

        #TO DO Pretty view

        # adding title to result string
        result_str = title +"\n"
        for el in self.ledger:
            result_str += str(el)+"\n"

        return result_str

def create_spend_chart(categories):
    print("TODOSpend chart")

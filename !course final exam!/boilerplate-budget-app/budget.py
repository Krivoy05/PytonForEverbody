class Category:
    leger = list()
    balance = 0

    def __init__(self, category):
        self.category = category

    def deposit(self, amount, description):
        #The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
        if description is Null:
            description = ""
        self.leger.append("\"amount\": "+str(amount)+", \"description\": "+description)
        self.balance += amount

    def withdraw(self, amount, description):
        #This method should return True if the withdrawal took place, and False otherwise.
        if self.balance >= amount:
            self.leger.append("\"amount\": "+str(-amount)+", \"description\": "+description)
            self.balance -= amount
            return True
        else:
            return False

    def get_balance(self, category):
        #returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
        return self.balance

    def get_transfer(self, amount, from_category):
        self.leger.append("\"amount\": " + str(amount) + ", \"Transfer to \": " + from_category)
        self.balance += amount

    def transfer(self, amount,target_category):
        """A transfer method that accepts an amount and another budget category as arguments.
         The method should add a withdrawal with the amount and the description
         "Transfer to [Destination Budget Category]". The method should then add a deposit to the other
         budget category with the amount and the description "Transfer from [Source Budget Category]".
          If there are not enough funds, nothing should be added to either ledgers."""
        if self.balance >= amount:
            self.leger.append("\"amount\": "+str(-amount)+", \"Transfer to \": "+target_category.category)
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

    def create_spend_chart(categories):
        print("TODOSpend chart")

food = Category("food")
water = Category("water")
food.deposit(200, "test deposit")
food.transfer(200, water)
print(food)
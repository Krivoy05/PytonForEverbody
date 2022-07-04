class Category:
    leger = list()
    balance = 0

    def __init__(self, category):
        self.category = category

    def deposit(self, amount, description):
        #The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
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
        #returns the current balance of the budget category based
        # on the deposits and withdrawals that have occurred.
        return 100

    def transfer(self, amount,category):
        """A transfer method that accepts an amount and another budget category as arguments.
         The method should add a withdrawal with the amount and the description
         "Transfer to [Destination Budget Category]". The method should then add a deposit to the other
         budget category with the amount and the description "Transfer from [Source Budget Category]".
          If there are not enough funds, nothing should be added to either ledgers."""

        # This method should return True if the transfer took place, and False otherwise.
        return True

    def check_funds(amount):
        """
        A check_funds method that accepts an amount as an argument.
        This method should be used by both the withdraw method and transfer method.
        :return:
        """

        # It returns False if the amount is greater than the balance of the budget category and
        #returns True otherwise.
        return True

    def create_spend_chart(categories):
        print("TODOSpend chart")

food = Category("food")
food.deposit(200, "test deposit")
food.withdraw(200,"test widraw")
print(food)
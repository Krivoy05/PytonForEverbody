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
        self.ledger.insert(0, {"amount": amount, "Transfer from":  from_category.category})
        self.balance += amount

    def transfer(self, amount, target_category):
        if self.balance >= amount:
            self.ledger.insert(0, {"amount": -amount, "Transfer to":  target_category.category})
            t_c = target_category.category
            target_category.get_transfer(amount, target_category)
            self.balance -= amount
            # This method should return True if the transfer took place, and False otherwise.
            return True
        else:
            return False

    def check_funds(self, amount):
        # It returns False if the amount is greater than the balance of the budget category and returns True otherwise.
        if amount <= self.balance:
            return True
        else:
            return False

    #Done pretty print
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

        #Done Pretty view

        # adding title to result string
        result_str = title +"\n"

        for el in self.ledger:
            #parse dictionary
            data = list()
            space_count = 0
            for value in el.values():
                data.append(value)
            for el in data:
                space_count += len(str(el))
            if space_count <= 30:
                result_str += data[1]
                for i in range(30 - space_count):
                    result_str += " "
            else:
                # if describe moe 30 symbols then cut describe
                possible_to_print_symbols = 30 - len(str(data[0]))
                result_str += data[1][0:possible_to_print_symbols]
                space_count = 0

            result_str += str(data[0]) + "\n"

        #Done Prety view
        result_str += "Total"
        spaces_count = 30 - (len("Total") + len(str(self.balance)))
        for i in range(spaces_count):
            result_str += " "
        result_str += str(self.balance)
        return result_str

def create_spend_chart(categories):
    print("TODOSpend chart")

f =Category("AAA")
f.deposit(-1000,"restaurant and more food for dessert")
print(f)
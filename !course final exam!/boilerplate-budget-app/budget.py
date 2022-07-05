class Category:
    ledger = list()
    balance = 0
    cost = 0

    def __init__(self, category):
        self.category = category
        self.ledger = list()

    def deposit(self, amount, *description):
        if isinstance(description,tuple):
            if len(description) == 1:
                description = description[0]
            else:
                description = ""
        #The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, *description):
        if isinstance(description, tuple):
            if len(description) == 1:
                description = description[0]
            else:
                description = ""
        #This method should return True if the withdrawal took place, and False otherwise.
        if self.balance >= amount:
            self.ledger.append( {"amount": -amount, "description": description})
            self.balance -= amount
            self.cost += amount
            return True
        else:
            return False

    def get_balance(self):
        #returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
        return self.balance

    def get_transfer(self, amount, target_category, from_category):
        target_category.ledger.append( {"amount": amount, "description": "Transfer from " + from_category})
        target_category.balance += amount

    def transfer(self, amount, target_category):
        if self.balance >= amount:
            self.ledger.append( {"amount": -amount, "description": "Transfer to " + target_category.category})
            target_category.get_transfer(amount, target_category , self.category)
            self.balance -= amount
            self.cost += amount
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
            data[0] = "{:.2f}".format(float(data[0]))
            for el in data:
                space_count += len(str(el))
            if space_count <= 30:
                result_str += data[1]
                for i in range(30 - space_count):
                    result_str += " "
            else:
                # if describe moe 30 symbols then cut describe
                possible_to_print_symbols = 30 - (len(str(data[0])) + 1)
                result_str += data[1][0:possible_to_print_symbols] + " "


            result_str += str(data[0]) + "\n"

        #Done Prety view
        result_str += "Total: "

        #  spaces_count = 30 - (len("Total") + len(str(self.balance)))
        #for i in range(spaces_count):
        #    result_str += "

        result_str += str(float(self.balance))
        return result_str

def create_spend_chart(categories):
    result_str = "Percentage spent by category\n"
    total_costs = 0
    procent_list = list()
    categorys_list = list()
    categorsy_count = 0
    for category in categories:
        total_costs += category.cost
        categorsy_count += 1
        categorys_list.append(category.category)

    longest_category_name = categorys_list[0]
    for category in categories:
        procent_list.append(category.cost*100//total_costs)
        if len(longest_category_name) < len(category.category):
            longest_category_name = category.category
    total_length = 5 + categorsy_count + categorsy_count * 2
    #print chart
    counter = 100
    while counter >= 0:
        if counter == 100:
            result_str += str(counter)+ "| "
        elif counter == 0:
            result_str += "  " + str(counter) + "| "
        else:
            result_str += " " + str(counter) + "| "
        for proc in procent_list:
            if proc >= counter:
                result_str += "o  "
            else:
                result_str += "   "
        result_str += "\n"
        counter -= 10

    #print dashes
    end_of_chart = "    "
    for i in range(total_length - 4):
        end_of_chart += "-"
    end_of_chart += "\n"
    #Print categorys
    for i in range(len(longest_category_name)):
        end_of_chart += "     "
        for el in categorys_list:
            if len(el) > i:
                end_of_chart += el[i] + "  "
            else:
                end_of_chart += "   "
        end_of_chart += "\n"
    #threre are no new line in test
    end_of_chart = end_of_chart[:-1]
    result_str += end_of_chart
    return result_str




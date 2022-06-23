class Arithmetic:
    def __init__(self,number1,number2,operation):
        self.number1 = number1
        self.number2 = number2
        self.operation = operation
        if operation in "+":
            self.result = str(int(number1) + int(number2))
        if operation in "-":
            self.result = str(int(number1) - int(number2))

class pretty_arithmetic:
    def __init__(self,number1,number2,dash,result):
        self.number1 = number1
        self.number2 = number2
        self.dash = dash
        self.result = result

def arithmetic_arranger(input_list, *print_result):
    arithmetic_list = parse_list(input_list)
    pretty_result_separate_operation = get_pretty_result(arithmetic_list)
    pretty_lines = get_separete_pretty_lines(pretty_result_separate_operation)
    result = get_result(pretty_lines,print_result)
    return result

def get_result(pretty_lines,is_print_result):
    result = ""
    if is_print_result:
        for el in pretty_lines:
            result += el
            result += "\n"
    else:
        for el in pretty_lines[0:len(pretty_lines) - 1]:
            result += el
            result += "\n"
    return result

def get_separete_pretty_lines(li):
    result_li = list()
    number1 = ""
    number2 = ""
    dash = ""
    result = ""
    for el in li:
        number1 += el.number1 + "    "
        number2 += el.number2 +  "    "
        dash    += el.dash    + "    "
        result  += el.result  + "    "

    result_li.append(number1)
    result_li.append(number2)
    result_li.append(dash)
    result_li.append(result)

    return result_li

def get_pretty_result(li):
    result = list()
    for ar in li:
        result_len = 0
        pretty_num1 = ""
        pretty_num2 = ""
        pretty_dash = ""
        pretty_result = ""
        num1_len = len(ar.number1)
        num2_len = len(ar.number2)
        if num1_len >= num2_len:
            result_len =  num1_len + 2

            #built pretty 1 number
            for i in range(result_len- num1_len):
                pretty_num1 += " "
            # Get complete pretty 1 number
            pretty_num1 += ar.number1

            #start buil prettu 2 nmber
            pretty_num2 += ar.operation
            for i in range(result_len - 1 - num2_len):
                pretty_num2 += " "
            # Get complete pretty 2 number
            pretty_num2 += ar.number2

            # build pretty dash
            for i in range(result_len):
                pretty_dash += "_"

            # built pretty result
            for i in range(result_len - len(ar.result)):
                pretty_result += " "
            pretty_result += ar.result

        else:
            result_len =  num2_len + 2
            # built pretty 1 number
            for i in range(result_len - num1_len):
                pretty_num1 += " "
            # Get complete pretty 1 number
            pretty_num1 += ar.number1

            # start buil prettu 2 nmber
            pretty_num2 += ar.operation
            for i in range(result_len - 1 - num2_len):
                pretty_num2 += " "
            # Get complete pretty 2 number
            pretty_num2 += ar.number2

            # build pretty dash
            for i in range(result_len):
                pretty_dash += "_"

            # built pretty result number
            for i in range(result_len - len(ar.result)):
                pretty_result += " "
            pretty_result += ar.result
        result.append(pretty_arithmetic(pretty_num1,pretty_num2,pretty_dash,pretty_result))
    return result

def input_lenth_check(li):
    result = False
    in_len = len(li)
    if in_len <= 5 and in_len>0:
        result = True
    else:
        raise Exception("Error: Too many problems.")
    return result

def is_all_elements_numbers(li):
    result = False
    for el in li:
        test = el.strip()
        if len(test)>4:
            raise Exception("rror: Numbers cannot be more than four digits.")
        if test.isdigit():
            result = True
        else:
            result = False
            raise Exception("Error: Numbers must only contain digits.")
    return result

def parse_list(li):
    #throw exeption if element more than 5 or list is empty
    input_lenth_check(li)
    result_li = list()
#split by + - , else throw exeption
    raw = list()
    for el in li:
        if "+" in el:
            raw = el.split("+")
            #check is it only numbers
            is_all_elements_numbers(raw)
            raw.append("+")
        elif "-" in el:
            raw = el.split("-")
            # check is it only numbers
            is_all_elements_numbers(raw)
            raw.append("-")
        else:
            raise Exception("Error: Operator must be '+' or '-'.")
        result_li.append(Arithmetic(raw[0].strip(),raw[1].strip(),raw[2]))
    return result_li



result = arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

print(result)
"""
Remove empty strings from a list of strings

Given:

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

Expected Output:

Original list of sting
['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']

After removing empty strings
['Emma', 'Jon', 'Kelly', 'Eric']
"""
def delete_from_list_with_epmty_data(input_list):
    result_list = []
    for list_value in input_list:
        try:
            if len(list_value) > 0:
                result_list.append(list_value)
        except:
            #do nothing
            result_list
    return result_list

def delete_from_list_with_epmty_data_test(input_list):
    result_list = []
    for list_value in input_list:
       if list_value:
          result_list.append(list_value)
    return result_list


str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
#print(delete_from_list_with_epmty_data_test(str_list))
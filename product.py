__author__ = 'zhaopeix'

# Assume the input is an int
find_product = lambda a : find_max(prod_of_every_five_digits(str(a)))

# this function will find the largest among the list
find_max = lambda lst : reduce((lambda a, b : a if a > b else b),lst)

# this function will calculate the product of a list of five digits
prod_of_five_digits = lambda five_digits_string : reduce(lambda a, b : int(a) * int(b), five_digits_string)

prod_of_every_five_digits = lambda int_str : map(prod_of_five_digits,all_five_digits_sub_strings(int_str))

# this function returns all the possible five consecutive digits in the number
all_five_digits_sub_strings = lambda int_str : map(lambda i : int_str[i:i+5],range(0,len(int_str)-5))



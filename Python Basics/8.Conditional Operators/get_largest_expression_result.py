# In this task, create a function get_largest_expression_result that accepts 2 numbers: a and b. 
# This function should compare the results of the following calculations and return the largest of them:

# a + b
# a - b
# a * b
# a / b
# Pay attention:
# numbers a and b can be negative
# a and b are not equal to zero
# do not use the math module, the ternary operator, or the else keyword.
# For example, if a = 10 and b = 5, then:
# a + b = 15
# a - b = 5
# a * b = 50 is the largest result
# a / b = 2
# But if a = 10 and b = -5, then:
# a + b = 5
# a - b = 15 is the largest result
# a * b = -50
# a / b = -2
# get_largest_expression_result(10, 5)  # 50
# get_largest_expression_result(10, -5)  # 15


# def get_largest_expression_result(a, b):
#     sum = a + b
#     dif = a - b
#     prod = a * b
#     share = a / b


#     if sum > dif:
#         if sum > prod:
#             if sum > share:
#                 return sum
#     if sum == dif or sum == prod or sum == share:
#         return sum

#     if dif > sum:
#         if dif > prod:
#             if dif > share:
#                 return dif
#     if dif == prod or dif == share:
#         return dif

#     if prod > sum:
#         if prod > dif:
#             if prod > share:
#                 return prod
#     if prod == share:
#         return prod

#     if share > sum:
#         if share > dif:
#             if share > prod:
#                 return share


def get_largest_expression_result(a, b):
    add_result = a + b
    sub_result = a - b
    mul_result = a * b
    div_result = a / b

    largest_result = add_result

    if sub_result > largest_result:
        largest_result = sub_result
    if mul_result > largest_result:
        largest_result = mul_result
    if div_result > largest_result:
        largest_result = div_result

    return largest_result

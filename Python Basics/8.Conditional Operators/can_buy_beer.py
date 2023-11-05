# # Create a function can_buy_beer that requires an integer age as a parameter:
# if the age is greater than or equal to 18, the function will return the string "You can buy beer"
# otherwise, the function will return the string "You can't buy beer".
# To return the desired string of functions, use the return keyword.
# example:
# can_buy_beer(17)  # "You can't buy beer"
# can_buy_beer(18)  # "You can buy beer"
# can_buy_beer(50)  # "You can buy beer"


def can_buy_beer(age: int) -> str:
    # write your code here
    if age >= 18:
        return "You can buy beer"
    else:
        return "You can not buy beer"


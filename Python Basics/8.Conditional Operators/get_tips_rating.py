# Implement the function get_tips_rating,
#  which accepts the amount of tips amount and returns a rating string according to the amount left:
# terrible, if the amount is UAH 0
# poor, if the amount is from 1 to 10 UAH inclusive
# good, if the amount is from 11 to 20 UAH inclusive
# great, if the amount is from 21 to 50 UAH inclusive
# excellent, if the amount is more than UAH 50.
# Example:
# def get_tips_rating(amount):
#     if amount == 0:
#          return "terrible"
#      if amount <= 10:
#          return "poor"
#      # add other conditions...
# get_tips_rating(0)  # "terrible"
# get_tips_rating(1)  # "poor"
# get_tips_rating(60) # "excellent"

def get_tips_rating(amount: int) -> str:

    if amount == 0:
        return "terrible"

    elif 1 <= amount <= 10:
        return "poor"

    elif 11 <= amount <= 20:
        return "good"

    elif 21 <= amount <= 50:
        return "great"

    elif amount > 50:
        return "excellent"

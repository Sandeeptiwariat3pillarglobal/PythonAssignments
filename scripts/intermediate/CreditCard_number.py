import re

PATTERN = '^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'


def is_valid_card_number(val):
    if type(val) not in [str]:
        return TypeError("Value should be String")
    else:
        match = re.match(PATTERN, val)

        if match is None:
            print("Invalid credit card number")
            return False
        else:
            print("Valid credit card number")
            return True

print(is_valid_card_number("4569999999999999"))
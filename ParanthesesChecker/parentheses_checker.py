#prog to check the balanced parentheses expression
def is_valid_pair(char1, char2):
    """This will check if the two character makes a valid pair"""
    if (char1 == '(' and char2 == ')') or\
        (char1 == '{' and char2 == '}') or \
        (char1 == '[' and char2 == ']'):
            return True
    else:
            return False

def check_balanced_parentheses(string):
    """It will check for the balanced parentheses in an expression"""
    paren = []
    for char in string:
        if char in ['(', '{', '[']:
            paren.append(char)
        elif char in [')', '}', ']']:
            if not paren or \
                not is_valid_pair(paren.pop(), char):
                return False
    #check if some unclosed parentheses left unpaired
    if paren:
        return False
    return True
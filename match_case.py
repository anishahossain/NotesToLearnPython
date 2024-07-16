import random

grade = 2  # variable grade from 1-5
match grade:  # grade variable used for match case function
    case 1:   # case operator matches the condition
        print('very good')  # and carries out specific output code
    case 2:
        print('good')
    case 3:
        print('average')
    case 4:
        print('bad')
    case 5:
        print('very bad')
    case _:  # underscore is 'wildcard' and carries out code when no match is found
        print('grade cannot be recognised')
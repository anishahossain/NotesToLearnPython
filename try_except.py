# example 1
def get_age():
    age = int(input())
    if 18 <= age <= 75:
        return age
    else:
        raise ValueError('Invalid age.')  # using raise like this

# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate = 0.7 * (220 - age)
    return heart_rate

if __name__ == "__main__":
    # try exception clock
    try:
        age = get_age()
        rate = fat_burning_heart_rate(age)
        print(f'Fat burning heart rate for a {age} year-old: {rate} bpm')
    except ValueError as expt:  # using the raise
        print(expt)
        print('Could not calculate heart rate info.')


# example 2
try:
    user_num = int(input())
    div_num = int(input())

    quotient = user_num // div_num
    print(quotient)

except ZeroDivisionError as z:  # no need to raise as auto-detected
    print(f"Zero Division Exception: {z}")

except ValueError as v:  # no need to raise as auto-detected
    print(f"Input Exception: {v}")
    # e.g. prints this
    # Input Exception: invalid literal for int() with base 10: 'user_num'
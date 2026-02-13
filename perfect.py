# Perfect Numbers
#num = int(input("Enter a number: "))

def numType(num):
    """ numType determine if input is either abundant, perfect, or deficient

    num : integer input; expects > 0

    returns:
    1 for abundant
    0 for perfect
    -1 for deficient
    """
    total = 1 # adding factor 1
    stop = int(num ** 0.5) + 1
    divider = 2
    while divider < stop:
        if num % divider == 0:
            # divider is a factor
            other = num // divider
            if divider != other:
                total += divider
                total += other
            else:
                total += divider
        divider += 1
    # end of while
    if total < num:
        # print(f"{num} is a deficient number.")
        return -1
    elif total > num:
        # print(f"{num} is an abundant number.")
        return 1
    else:
        # print(f"{num} is a perfect number.")
        return 0
# end of numType()

value = 2
perfect_sum = 0
while value <= 1000000:
    if numType(value) == 0:
        # numType() returned a perfect result
        perfect_sum += value
    value += 1

print(f"Total sum of all perfect number under 1000000: {perfect_sum}")











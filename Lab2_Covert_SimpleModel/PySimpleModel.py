# Mayolo Valencia
# This program takes an input then converts the float input
# into a simple model number.

def convert_to_fp(num):
    # Check if the number is negative
    sign_bit = '1' if num < 0 else '0'

    # Convert the number to absolute value and split into integer and fractional parts
    num = abs(num)
    int_part = int(num)
    frac_part = num - int_part

    # Convert the integer part to binary form
    # [2:] is slice notation because the bin output is 0b and is useless
    int_bin = bin(int_part)[2:]

    # Convert the fractional part to binary form with only 4 bits
    frac_bin = ''
    for i in range(4):
        frac_part *= 2
        frac_bit = int(frac_part)
        frac_bin += str(frac_bit)
        frac_part -= frac_bit

    # Combine the integer and fractional parts to form the mantissa
    mantissa = int_bin + frac_bin

    # Calculate the exponent using the bias of 15
    exponent = len(int_bin) - 1 + 15

    # Convert the exponent to binary form
    exponent_bin = bin(exponent)[2:].zfill(5)

    # Combine the sign bit, exponent, and mantissa to form the final floating-point representation
    fp = sign_bit + exponent_bin + mantissa

    return fp

while True :
    
    while True:
        try:
            user_num = float(input("Input float number here: "))
            break
        except ValueError:
            print("Please input numbers only...") 
            continue
    
    fp = convert_to_fp(user_num)
    print(fp)
    
    continueLoop = input("Do you want to continue? (y/n) ")
    if continueLoop == 'n':
        break

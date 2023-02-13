# Mayolo Valencia
# This program takes a users input of either a binary or decimal number
# There is a Try/Catch to verify the users input and ask them again to
# input their values correctly. The value gets passed to 4 functions (actively 3)
# they convert the number to binary, decimal, hexidecimal, and octal. 

import math

# input should be in decimal for this one
def convert_to_binary(num):
    # create list to hold binary values
    binary_list= []
    
    # convert decimal to binary
    while num != 0:
        
        if num%2 == 1:
            binary_list.append('1')
        else:
            binary_list.append('0')
        num = num//2
    
    # reverse list
    binary_list.reverse()
    # join the list to a string and cast to integer
    num = int(''.join(binary_list))
    return num

# Decimal to Octal
def convert_to_octal(num):
    
    # create list to hold octal values
    octal_list= []
    
    # convert decimal to octal
    while num != 0:
        octal_list.append(str(num%8))
        num = num//8
    
    # reverse list
    octal_list.reverse()
    # join the list to a string and cast to integer
    num = int(''.join(octal_list))
    return num

# Decimal to Hexidecimal
def convert_to_hex(num):
    
    # create list to hold hexidecimal values
    hex_list= []

    remainder = 0
    while num != 0:
        
        if num%16 == 10:
            hex_list.append('A')
        elif num%16 == 11:
            hex_list.append('B')
        elif num%16 == 12:
            hex_list.append('C')
        elif num%16 == 13:
            hex_list.append('D')
        elif num%16 == 14:
            hex_list.append('E')
        elif num%16 == 15:
            hex_list.append('F')
        else:
            remainder = num%16
            # add remainder to hexidecimal list
            hex_list.append(str(remainder))
    
        num = num//16
        
    # reverse list
    hex_list.reverse()
    # join list values to a string
    num = ''.join(hex_list)
    return num  

# input should be in binary for this one
def convert_to_decimal(num):
    binary_list = list(str(num))
    decimal_number = 0
    
    # holds the exponent value
    oneCounter = len(binary_list)-1

    # iterate through the list and add each digit to the decimal number.
    for i in binary_list:
        if(i == '1'):
            decimal_number += math.pow(2, oneCounter)
        oneCounter+=-1            
    return decimal_number


while True :
    
    while True:
        try:
            user_num = int(input("Enter number in binary or decimal:"))
            break
        except ValueError:
            print("Please input numbers only...") 
            continue

    binary_or_decimal = int(input("Choose:\n0 if decimal\n1 if binary\nInput here: "))
    if binary_or_decimal == 0:
        print("\nThis is your number:", user_num,"and its a decimal number")
        print("Binary:",convert_to_binary(user_num))
        print("Hexadecimal:", convert_to_hex(user_num))
        print("Octal:",convert_to_octal(user_num))
    elif binary_or_decimal == 1:
        print("This is your number:", user_num,"and its a binary number")
        binary_in_decimal = convert_to_decimal(user_num)
        print("Decimal:", binary_in_decimal)
        print("Hexadecimal:", binary_in_decimal)
        print("Octal:", binary_in_decimal)

    choice = input("Do you want to go again yes(1) or no(0)")
    
    if choice == '0':
        break

print("end of cycle, thank you.")
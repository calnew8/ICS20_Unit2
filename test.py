#Get two digit integer from user
s_two_digit_in = input("Please enter a two-digit integer: ")
#Integer conversion
i_two_digit_in = int(s_two_digit_in)
#Modulus math to get digits
ones_digit = i_two_digit_in % 10
tens_digit = int((i_two_digit_in - ones_digit)/10)
#output digits
print("The first digit is:\t",tens_digit,"\nThe second digit is:\t",ones_digit)
import statistics
import math

#Problem 1

print("\nProblem 1:\n")
s_side1 = input("Enter the legnth of the first side: \t")
s_side2 = input("Enter the legnth of the second side: \t")
f_side1 = float(s_side1)
f_side2 = float(s_side2)
perimiter = (f_side1*2)+(f_side2*2)
area = f_side1*f_side2
print("Perimiter:\t",perimiter,"\nArea:\t\t",area)

#Problem 2

print("\nProblem 2\n")
s_celcius = input("Enter the tempertaure in celsius: \t ")
f_celcius = float(s_celcius)
farenheit = (f_celcius*1.8)+32
print("The tempertaure in farenheit is:\t","{0:,.0f}".format(farenheit))

#Problem 3

print("\nProblem 3\n")
s_farenheit = input("Enter the tempertaure in farenheit: \t ")
f_farenheit = float(s_farenheit)
celcius = (f_farenheit-32)/1.8
print("The tempertaure in celcius is:\t\t","{0:,.0f}".format(celcius))

#Problem 4

'''
Input: Distance of each of 4 long jumps
Processing: Add up all 4 long jump legnths, calculate average of long jumps (sum of jumps/number of jumps)
Output: Sum and average of long jumps
'''

print("\nProblem 4\n")
s_jump1 = input("Enter the legnth of your first jump:")
s_jump2 = input("Enter the legnth of your second jump:")
s_jump3 = input("Enter the legnth of your third jump:")
s_jump4 = input("Enter the legnth of your fourth jump:")
f_jump1 = float(s_jump1)
f_jump2 = float(s_jump2)
f_jump3 = float(s_jump3)
f_jump4 = float(s_jump4)
avgjump = statistics.mean((f_jump1,f_jump2,f_jump3,f_jump4))
totaljump = f_jump1+f_jump2+f_jump3+f_jump4
print("Your average jump legnth is:\t",avgjump)
print("Your total jump legnth is:\t",totaljump)

#Problem 5

print("\nProblem 5\n")
obj_name = input("What is the name of the item you are buying?")
s_obj_cost = input('How much does a '+obj_name+' cost?')
s_obj_count = input("How many "+obj_name+" are you buying?")
f_obj_cost = float(s_obj_cost)
i_obj_count = int(s_obj_count)
no_tax_cost = f_obj_cost*i_obj_count
only_tax_cost = f_obj_cost*i_obj_count*0.13
tax_cost = f_obj_cost*i_obj_count*1.13
print("Total before tax:\t\t","${0:,.2f}".format(no_tax_cost))
print("Amount of tax:\t\t\t","${0:,.2f}".format(only_tax_cost))
print("Total after tax:\t\t","${0:,.2f}".format(tax_cost))
s_paying_amount = input("Please enter the amount you will be paying:")
f_paying_amount = float(s_paying_amount)
change_due = f_paying_amount-tax_cost
if change_due >= 0:
	print("Change due:","${0:,.2f}".format(change_due))
else:
	print("The amount you have entered is less than the price of the items you wish to buy. \nPlease talk to a human by pressing the green button on the left of the machine. \nLocking room door to prevent theft")
	
#Problem 6

'''
Input: Two numbers, to be used in equations (e.g. number1 + number2)
Processing: Calculate sum, diffrence, product, quotient, modulus, number raised to power
Output: Print numbers, sum, difference, product, quotient, modulus, number raised to power
'''

print("\nProblem 6\n")
#get two numbers
s_number_first = input("Please enter the first number: ")
s_number_second = input("Please enter the second number:")
#convert numbers to floats
f_number_first = float(s_number_first)
f_number_second = float(s_number_first)
#math
sum_numbers = f_number_first + f_number_second
diff_numbers = f_number_first - f_number_second
product_numbers = f_number_first * f_number_second
quo_numbers = f_number_first / f_number_second
mod_numbers = f_number_first % f_number_second
pow_numbers = math.pow(f_number_first,f_number_second)
#print stuff
print(f_number_first," + ",f_number_second," = ",sum_numbers)
print(f_number_first," - ",f_number_second," = ",diff_numbers)
print(f_number_first," * ",f_number_second," = ",product_numbers)
print(f_number_first," / ",f_number_second," = ",quo_numbers)
print(f_number_first," % ",f_number_second," = ",mod_numbers)
print(f_number_first," ^ ",f_number_second," = ",pow_numbers)

#Problem 7

'''
Input: Amount of change less than 1 dollar
Processing: amount of change integer (floor) divided by 25 to get amount of quarters, amount of change % 25 to get remainder. Remainder from quarters integer (floor) divided by 10 to get amount of dimes, remainder from quarters % 10 to get remainder. Remainder from dimes integer (floor) divided by 5 to get amount of nickels, remainder from dimes % 5 to get remainder. Remainder from nickels integer (floor) divided by 1 to get amount of pennies.
Output: Minimum number of pennies, nickels, quarters needed to make change
'''

print("\nProblem 7\n")
#get amount of change less than 1 dollar
s_changetotal = input("Enter an amount of change less than 1 dollar in decimal: ")
#convert to float
f_changetotal_unround_dec = float(s_changetotal)
#round to 2 decimal places
f_changetotal_dec = round(f_changetotal_unround_dec,2)
#multiply by 100 to get number of cents
f_changetotal = f_changetotal_dec * 100
#quarter math
quarter_amount = f_changetotal // 25
quarter_remainder = f_changetotal % 25
#dime math
dime_amount = quarter_remainder // 10
dime_remainder = quarter_remainder % 10
#nickel math
nickel_amount = dime_remainder // 5
nickel_remainder = dime_remainder % 5
#NOTE: Nickel remainder doubles as amount of pennies
#Print numbers
print("Pennies:\t",nickel_remainder,"\nNickels:\t",nickel_amount,"\nDimes:\t\t",dime_amount,"\nQuarters:\t",quarter_amount)

#Problem 8

'''
Input: Two digit integer
Processing: 
Output: Seperate digits from one and tens place from input number
'''



#Get two digit integer from user
s_two_digit_in = input("Please enter a two-digit integer: ")
#Integer conversion
i_two_digit_in = int(s_two_digit_in)
#Modulus math to get digits
ones_digit = i_two_digit_in % 10
tens_digit = int((i_two_digit_in - ones_digit)/10)
#output digits
print("The first digit is:\t",tens_digit,"\nThe second digit is:\t",ones_digit)
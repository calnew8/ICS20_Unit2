import math
import statistics
'''
Callum Newby-Clark
21/09/2018
Solving predefined math problems
'''
'''
prob_num = 0
def print_prob_num(prob_num):
    print("Problem Number ", prob_num,"\n")
    prob_num += 1
    return prob_num
'''
#Problem 1

print("----------------------------------------------------------------------------\nPROBLEM 1:\n")
num_add1 = 3
num_add2 = 10
sum_num = num_add1 + num_add2
print(num_add1, " + ", num_add2, " = ", sum_num)

#problem 2 

print("----------------------------------------------------------------------------\nPROBLEM 2:\n")
num_subtract1 = 14
num_subtract2 = 6
difference = num_subtract1 - num_subtract2
print(num_subtract1, " - ", num_subtract2, " = ", difference)

#problem 3

print("----------------------------------------------------------------------------\nPROBLEM 3:\n")
widgets_per_day = 1022957
widgets_per_pack = 12
total_full_boxes = "{0:,.1f}".format(widgets_per_day//widgets_per_pack)
amnt_partial_box = widgets_per_day % widgets_per_pack
print("Widgets per day:\t",widgets_per_day,"\nWidgets per pack:\t",widgets_per_pack,"\nTotal full boxes:\t",total_full_boxes,"\nTotal partial boxes:\t",amnt_partial_box)

#problem 4

print("----------------------------------------------------------------------------\nPROBLEM 4:\n")
percent_smallnum1 = 10
percent_smallnum2 = 20
percent_smallnum3 = 5
percent_bignum1 = 70
percent_bignum2 = 25
percent_bignum3 = 60
print(percent_smallnum1, "% of", percent_bignum1, "is", percent_smallnum1*percent_bignum1/100)
print(percent_smallnum2, "% of", percent_bignum2, "is", percent_smallnum2*percent_bignum2/100)
print(percent_smallnum3, "% of", percent_bignum3, "is", percent_smallnum3*percent_bignum3/100)

#problem 5

print("----------------------------------------------------------------------------\nPROBLEM 5:\n")
hours_per_week = 40
dollars_per_hour = 9.58
overtime_pay_multiplier = 1.50
hours_worked = 52
overtime_rate = dollars_per_hour*overtime_pay_multiplier
overtime_hours = hours_worked-hours_per_week
regular_pay = hours_per_week*dollars_per_hour
overtime_pay = overtime_hours*(overtime_rate)
total_pay = regular_pay + overtime_pay
print("Total hours:\t\t",hours_worked,"\nRegular hours:\t\t",hours_per_week,"\nOT hours:\t\t",overtime_hours)
print("Regular Rate:\t\t","${0:,.2f}".format(dollars_per_hour),"\nOT rate:\t\t","${0:.2f}".format(overtime_rate),"\nTotal Regular Pay:\t","${0:.2f}".format(regular_pay),"\nTotal OT Pay:\t\t","${0:.2f}".format(overtime_pay),"\nTotal Pay:\t\t","${0:.2f}".format(total_pay))

#problem 6

print("----------------------------------------------------------------------------\nPROBLEM 6:\n")
math_grade = 95
programming_grade = 98
science_grade = 92
english_grade = 88
average_grade = statistics.mean([math_grade, programming_grade, science_grade, english_grade])
print("Math:\t\t\t","{0:}%".format(math_grade),"\nProgramming\t\t","{0:}%".format(programming_grade),"\nScience\t\t\t","{0:}%".format(science_grade),"\nEnglish\t\t\t","{0:}%".format(english_grade),"\nAverage\t\t\t","{0:}%".format(average_grade))

#problem 7

print("----------------------------------------------------------------------------\nPROBLEM 7:\n")
original_cost = 62.99
final_cost = 71.81
amnt_tax = final_cost-original_cost
rate_tax = (final_cost/original_cost)-1
print("Original Cost \t\t","${0:.2f}".format(original_cost),"\nFinal Cost\t\t","${0:.2f}".format(final_cost),"\nAmount of tax\t\t","${0:.2f}".format(amnt_tax),"\nTax Rate\t\t","{0:}%".format(rate_tax))
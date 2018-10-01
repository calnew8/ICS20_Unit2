'''
Callum Newby-Clark
25/09/2018
A program to calculate fuel efficency for a road trip
'''
#Calculate fuel efficency in mpg when given miles and gallon use
s_miles = input("Enter the distance in miles:")
s_gallons = input("Enter the fuel burned in gallons:")
#convert values to floats
f_miles = float(s_miles)
f_gallons = float(s_gallons)
#math
miles_per_gallon = f_miles/f_gallons
#print
print("Your Miles Per Gallon:","{0:,.2f}".format(miles_per_gallon))

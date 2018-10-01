import math
'''
Callum Newby-Clark
21/09/2018
Formatting Demo
'''

#set up variable that we know contains a long decimal number
knownnumber = math.sqrt(2)*math.pow(10,7)
#standard output
print (knownnumber)
#round to 4 decimal places
roundedknownnumber = "{0:,.4f}".format(knownnumber)
print (roundedknownnumber)
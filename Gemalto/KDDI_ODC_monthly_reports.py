##!/usr/bin/python
def UserInput():
    print "*********************************************************************************"
    print "* \t This script will generate MNO Monthly report for KDDI ODC LAB(ENI182) \t*"
    print "*********************************************************************************"
    print "\n"
    month = raw_input("Enter month in format of \"MM\" : " )
    year = raw_input("Enter year in format of \"YYYY\" : " )
    return month, year 
        
def Validate_Month_Year(month, year):
    try:
        m = int(month)
        if m in range(1,13) and \
            int(year) >= 2015 and \
            int(year) <= 2999:
            print "OK"
            correct()
        else:
            print "[ERROR] :\nIncorrect input; \nUsage : month = MM and year = YYYY"
    except:
           print "[ERROR] :\nIncorrect input; \nUsage : month = MM and year = YYYY"

def correct():
    m = int(month)
    MM = '%02d' % m
    print MM
    print year

month, year = UserInput()

Validate_Month_Year(month, year)




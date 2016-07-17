from scipy.constants.constants import year
def UserInput():
    print "*********************************************************************************"
    print "* \t This script will generate MNO Monthly report for KDDI ODC LAB(ENI182) \t*"
    print "*********************************************************************************"
    print "\n"
    month = raw_input("Enter month in format of \"MM\" : " )
    year = raw_input("Enter year in format of \"YYYY\" : " )
    return month, year
    
def validate_month_year(month, year):
    try:
        m = int(month)
        if m in range(1,13) and \
            int(year) >= 2015 and \
            intern(year) <= 2050:
            print "OK"
        else:
            print "[ERROR] :\nIncorrect input; \nUsage : month = MM and year = YYYY"
    except:
        print "[ERROR] :\nIncorrect input; \nUsage : month = MM and year = YYYY"

month, year = UserInput()

validate_month_year(month, year)

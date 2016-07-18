#!/usr/bin/python
from subprocess import Popen, PIPE

def UserInput():
    print "*********************************************************************************"
    print "* \t This script will generate MNO Monthly report for KDDI ODC LAB(ENI182) \t*"
    print "*********************************************************************************"
    print "\n"
    month = raw_input("Enter month in format of \"MM\" : " )
    year = raw_input("Enter year in format of \"YYYY\" : " )
    return month, year

def Validate_Month_Year(month, year):
    proceed = 1
    try:
        m = int(month)
        if m in range(1,13) and \
            int(year) >= 2015 and \
            int(year) <= 2999:
            proceed = 0
        else:
            print "[ERROR] :\tIncorrect input \nUsage : month = MM and year = YYYY"
    except:
           print "[ERROR] :\tIncorrect input \nUsage : month = MM and year = YYYY"
    return proceed
	
def generate_report():
    # Convert month in to two digit value
    m = int(month)
    MM = '%02d' % m
	
    # Define report file name
    filename="MNO_Report_KDDI_ODC_LAB_%s_%s.csv" % (MM, year)
	
    # set MNO list and  Start / End Date values
    MNO_LIST=['1.3.6.1.4.1.47238','1.3.6.1.4.1.47238']
    StartDate = "%s-%s-01T00:00:00" % (year, MM)
    EndDate = "%s-%s-31T23:59:59"  % (year, MM)

    FILE=open(filename,"w");

    # Set up SQL connection
    connectString = 'osmsrkddi_3035/f75PhD0HMNuVA5lw5@OSMSR_KDDI.PROD.GEMPLUS.COM'
    
    def runSqlQuery(sqlCommand, connectString):
	session = Popen(['sqlplus', '-S', connectString], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	session.stdin.write(sqlCommand)
	return session.communicate()
	
    # Writing Header to the report file 	
    FILE.write("MNO_NAME\t,USE_CASE\t,SUCCESS_COUNT\t,FAILED_COUNT\n")

    for i in MNO_LIST:
	if i == '1.3.6.1.4.1.47238':
		sqlCommandSuccess = '@test1.sql %r %r %r' % (i, StartDate, EndDate)
		# Successful Count
                queryResultSuccess, errorMessage = runSqlQuery(sqlCommandSuccess, connectString)
                ResultSuccess = queryResultSuccess.strip()
                # Failed Count
                sqlCommandFailed = '@test2.sql %r %r %r' % (i, StartDate, EndDate)
                queryResultFailed, errorMessage = runSqlQuery(sqlCommandFailed, connectString)
                ResultFailed = queryResultFailed.strip()
                FILE.write("KDD\t,Enable\t,%s\t,%s\n" % (ResultSuccess, ResultFailed))
        else:
                print "OK"

    FILE.close()		

month, year = UserInput()

proceed = Validate_Month_Year(month, year)

if proceed == 0:
	generate_report()
else:
	exit(0)

exit(0)

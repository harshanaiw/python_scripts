#!/usr/bin/python
from subprocess import Popen, PIPE
import calendar

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
    EOM = calendar.monthrange(int(year), m)[1]
    MM = '%02d' % m
	
    # Define report file name
    filename="Reports/MNO_Report_KDDI_ODC_LAB_%s_%s.csv" % (MM, year)
	
    # set MNO list and  Start / End Date values
    MNO_LIST=['1.3.6.1.4.1.2054','1.3.6.1.4.1.47238','1.3.6.1.4.1.2054.1','1.3.6.1.4.1.47306']
    StartDate = "%s-%s-01T00:00:00" % (year, MM)
    EndDate = "%s-%s-%sT23:59:59"  % (year, MM, EOM)

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
		if i == '1.3.6.1.4.1.2054':
			# Successful Profile Enable Count FOR KDDI
			sqlCommandSuccess = '@SQL/subscription_count.sql %r %r %r UC_SubscriptionEnable SUCCEEDED ' % (i, StartDate, EndDate)
			queryResultSuccess, errorMessage = runSqlQuery(sqlCommandSuccess, connectString)
                	ResultSuccess = queryResultSuccess.strip()
        	        
			# Failed Profile Enable Count FOR KDDI
	                sqlCommandFailed = '@SQL/subscription_count.sql %r %r %r UC_SubscriptionEnable FAILED ' % (i, StartDate, EndDate)
                	queryResultFailed, errorMessage = runSqlQuery(sqlCommandFailed, connectString)
        	        ResultFailed = queryResultFailed.strip()
	                FILE.write("KDD\t,Profile_Enable\t,%s\t,%s\n" % (ResultSuccess, ResultFailed))
	
		elif i == '1.3.6.1.4.1.2054.1':
			# Successful Profile Enable Count FOR KDJ
			sqlCommandSuccess = '@SQL/subscription_count.sql %r %r %r UC_SubscriptionEnable SUCCEEDED ' % (i, StartDate, EndDate)
			queryResultSuccess, errorMessage = runSqlQuery(sqlCommandSuccess, connectString)
	                ResultSuccess = queryResultSuccess.strip()
        
		        # Failed Profile Enable Count FOR KDJ
                	sqlCommandFailed = '@SQL/subscription_count.sql %r %r %r UC_SubscriptionEnable FAILED ' % (i, StartDate, EndDate)
	                queryResultFailed, errorMessage = runSqlQuery(sqlCommandFailed, connectString)
        	        ResultFailed = queryResultFailed.strip()
                	FILE.write("KDJ\t,Profile_Enable\t,%s\t,%s\n" % (ResultSuccess, ResultFailed))
	        elif i == '1.3.6.1.4.1.47238':
			# Successful Profile Enable Count FOR AIS
	                sqlCommandSuccess = '@SQL/subscription_count.sql %r %r %r UC_SubscriptionEnable SUCCEEDED ' % (i, StartDate, EndDate)
			queryResultSuccess, errorMessage = runSqlQuery(sqlCommandSuccess, connectString)
        	        ResultSuccess = queryResultSuccess.strip()
	
	                # Failed Profile Enable Count FOR AIS
                	sqlCommandFailed = '@SQL/subscription_count.sql %r %r %r UC_SubscriptionEnable FAILED ' % (i, StartDate, EndDate)
        	        queryResultFailed, errorMessage = runSqlQuery(sqlCommandFailed, connectString)
	                ResultFailed = queryResultFailed.strip()
                	FILE.write("AIS\t,Profile_Enable\t,%s\t,%s\n" % (ResultSuccess, ResultFailed))
		
			# Successful Profile Download Count FOR AIS
                	sqlCommandDOWNSuccess = '@SQL/subscription_count.sql %r %r %r UC_DownloadProfile SUCCEEDED ' % (i, StartDate, EndDate)
			queryResultDOWNSuccess, errorMessage = runSqlQuery(sqlCommandDOWNSuccess, connectString)
             		ResultDOWNSuccess = queryResultDOWNSuccess.strip()
                	
			# Failed Profile Download Count FOR AIS
                	sqlCommandDOWNFailed = '@SQL/subscription_count.sql %r %r %r UC_DownloadProfile FAILED ' % (i, StartDate, EndDate)
                	queryResultDOWNFailed, errorMessage = runSqlQuery(sqlCommandDOWNFailed, connectString)
                	ResultDOWNFailed = queryResultDOWNFailed.strip()
                	FILE.write("AIS\t,Profile_Download\t,%s\t,%s\n" % (ResultDOWNSuccess, ResultDOWNFailed))
		
		elif i == '1.3.6.1.4.1.47306':	
			# Successful Profile Enable Count FOR JCC
                	sqlCommandSuccess = '@SQL/subscription_count.sql %r %r %r UC_SubscriptionEnable SUCCEEDED ' % (i, StartDate, EndDate)
			queryResultSuccess, errorMessage = runSqlQuery(sqlCommandSuccess, connectString)
                	ResultSuccess = queryResultSuccess.strip()
        	
		        # Failed Profile Enable Count FOR JCC
	                sqlCommandFailed = '@SQL/subscription_count.sql %r %r %r UC_SubscriptionEnable FAILED ' % (i, StartDate, EndDate)
                	queryResultFailed, errorMessage = runSqlQuery(sqlCommandFailed, connectString)
        	        ResultFailed = queryResultFailed.strip()
	                FILE.write("JCC\t,Profile_Enable\t,%s\t,%s\n" % (ResultSuccess, ResultFailed))
		
			# Successful Profile Download Count FOR JCC
                	sqlCommandDOWNSuccess = '@SQL/subscription_count.sql %r %r %r UC_DownloadProfile SUCCEEDED ' % (i, StartDate, EndDate)
			queryResultDOWNSuccess, errorMessage = runSqlQuery(sqlCommandDOWNSuccess, connectString)
                	ResultDOWNSuccess = queryResultDOWNSuccess.strip()
                	
			# Failed Profile Download Count for JCC
        	        sqlCommandDOWNFailed = '@SQL/subscription_count.sql %r %r %r UC_DownloadProfile FAILED ' % (i, StartDate, EndDate)
	                queryResultDOWNFailed, errorMessage = runSqlQuery(sqlCommandDOWNFailed, connectString)
                	ResultDOWNFailed = queryResultDOWNFailed.strip()
        	        FILE.write("JCC\t,Profile_Download\t,%s\t,%s\n" % (ResultDOWNSuccess, ResultDOWNFailed))	
		
		else:
	                print "[ERROR:] Invalid parameter passed to generate report.."

    FILE.close()	
    return filename	

# Calling UserInput to enter Month and Year for the report
month, year = UserInput()

# Check the entered values are correct and if yes, proceeding to generate report
proceed = Validate_Month_Year(month, year)

if proceed == 0:
	filename = generate_report()
	print "Report Generated !!!\nReport_file : %s " % (filename)
else:
	exit(0)

exit(0)

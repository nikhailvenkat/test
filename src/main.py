import time
import os
import re
from test1 import test1
from test2 import test2
#from interfaceState import *

testCase = {}

def adjustLine (line, space, spChar):
	
	lineLength = len(line)
	restSpace = space - lineLength
	zeroOrOne = restSpace % 2
	spaceCount = restSpace / 2
	initStr = spChar
	initStr = initStr+" "*spaceCount
	endStr = " "*(spaceCount+zeroOrOne)		
	endStr = endStr + spChar
	adjustedLine = initStr+line+endStr
	return adjustedLine



def printSummaryReport(fp):
	
	#global testId
	#global testCase
	
	gap = 26
	
	fp.write("\n=========================== BT VPN Edge Automation Summary Report =============================\n")
	fp.write(adjustLine('TestCase', gap, '|'))
	fp.write(adjustLine('TestResult', gap, '|'))
	fp.write(adjustLine('TotalTime(HH:MM:SS)', gap, '|'))
	fp.write("\n====================================================================================\n")
	
	id = 1
	while id<testId:
		fp.write(adjustLine(testCase[str(id)+'_name'], gap, '|'))
		fp.write(adjustLine(testCase[str(id)+'_result'], gap, '|'))
		fp.write(adjustLine(testCase[str(id)+'_time'], gap, '|'))
		fp.write("\n")
		
		id = id + 1
		
		
	fp.write("\n====================================================================================\n")
	
	return
	

def getTotalTime(startTime, endTime):
	""" Returns Total Time taken to execute each test case """
	hourDif = 0
	minuteDif = 0
	secondDif = 0
	highSecond = 0
	highMinute = 0
	
	rxStTime = re.match("(\S+)_(\S+)_(\S+)", startTime)
	rxEnTime = re.match("(\S+)_(\S+)_(\S+)", endTime)
	
	(stHour, stMinute, stSecond ) = rxStTime.groups()
	(enHour, enMinute, enSecond ) = rxEnTime.groups()
		
	"""scan $stHour %d stHour
	scan $stMinute %d stMinute
	scan $stSecond %d stSecond
	scan $enHour %d enHour
	scan $enMinute %d enMinute
	scan $enSecond %d enSecond"""
	
	if stSecond > enSecond:
		secondDif =  ((60 - int(stSecond)) + int(enSecond))
		highSecond = 1
	elif stSecond != enSecond:
		secondDif = int(enSecond) - int(stSecond)
	
	
	if stMinute > enMinute:
		if highSecond == 0:
			minuteDif = ((60 - int(stMinute)) + int(enMinute))
		else:
			minuteDif = (((60 - int(stMinute)) + int(enMinute)) - 1)
		
		highMinute = 1
	elif stMinute != enMinute: 
		if (highSecond == 0): 
			minuteDif = int(enMinute) - int(stMinute)
		else:
			minuteDif = ((int(enMinute) - int(stMinute)) - 1)
		
	
	
	if (stHour > enHour):
		if highMinute == 0:
			hourDif = ((60 - int(stHour)) + int(enHour))
		else: 
			hourDif = (((60 - int(stHour)) + int(enHour)) - 1)
		
	elif stHour != enHour:
		if highMinute == 0: 
			hourDif = int(enHour) - int(stHour)
		else: 
			hourDif = ((int(enHour) - int(stHour)) - 1)
		
	
	
	if re.match("\d", str(hourDif)):
		newHourDif = 0
		newHourDif = str(newHourDif)+str(hourDif)
		hourDif = newHourDif
	
	
	if re.match("\d", str(minuteDif)):
		newMinuteDif = 0
		newMinuteDif = str(newMinuteDif)+str(minuteDif)
		minuteDif = newMinuteDif
	
	
	if re.match("\d", str(secondDif)):
		newSecondDif = 0
		newSecondDif = str(newSecondDif)+str(secondDif)
		secondDif = newSecondDif
	
	
	return hourDif+':'+minuteDif+':'+secondDif


	

	
""" Test case execution starts from here """
	
print "\n===================================================================="
print "|                  BT VPN Edge Automation Test Execution Started                  |"
print "====================================================================\n"

"""
Open the file : testScriptList from which we need to get the test cases to be executed.
create a directory where the summary report and individual test case report gets stored.
create the summary report file  
"""
fp = open("testScriptList.txt", "r")
logDirName = time.strftime("%d_%m_%Y_%H_%M_%S")
os.mkdir( "../logs/"+logDirName )
#os.mkdir( logDirName )
sumRepFp = open("../logs/"+logDirName+"/"+"summaryReport.txt", "w")

testId = 1
line = fp.readline()
while line != "":
	
	if re.match("\#.*", line):
		pass
	else:
		name = line		
		testCase[str(testId)+"_name"] = name
		print "TestCase: %s" %(testCase[str(testId)+"_name"])
		startTime = time.strftime("%H_%M_%S")
		testCase[str(testId)+"_result"] = eval(line)()
		print testCase[str(testId)+"_result"]
		if testCase[str(testId)+"_result"] == 1:
			testCase[str(testId)+"_result"] = "Pass"
		else:
			testCase[str(testId)+"_result"] = "Fail"
		
		print "Result: %s" %(testCase[str(testId)+"_result"])
		endTime =  time.strftime("%H_%M_%S")
		testCase[str(testId)+"_time"] = getTotalTime(startTime, endTime)
		print "Total Time: %s" %(testCase[str(testId)+"_time"])
	
		testId = testId + 1
	line = fp.readline()
	
printSummaryReport(sumRepFp)

fp.close()
sumRepFp.close()


		
				
		
		
		
	
	
	
	

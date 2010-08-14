#!/usr/bin/python

import sys,getpass,cookielib,urllib2

print "Welcome. Enter your mycantos username & password to send free SMS."
userid=raw_input("Enter username: ")
password=getpass.getpass()
open_sock=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
try:
	open_sock.open('http://www.mycantos.com/','username='+userid+'&password='+password+'&checklogin=1')
except IOError:
	print "Error accessing www.mycantos.com.\nExiting program."
	sys.exit()
print "Logged into mycantos as "+userid+"."
open_sock.open('http://www.mycantos.com/sendSMS.php')
print "Prepare your message and phone number to send."
open_sock.addheaders=[('Referer','http://www.mycantos.com/sendSMS.php'),('User-Agent','Mozilla/6.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Ubuntu/10.04 (lucid) Firefox/3.6.8 GTB7.0')]
sms=raw_input("Enter your sms: ")
numb=raw_input("Enter recipient number: ")
try:
	open_sock.open('http://www.mycantos.com/sendSMStoanyone.php','checkSMS=1&SMSnumber='+numb+'&SMSmessage='+sms)
except IOError:
	print "Error sending SMS\nExiting program."
	sys.exit()
open_sock.close();
print "SMS SENT to "+numb+"."

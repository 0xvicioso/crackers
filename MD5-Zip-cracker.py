#Very Simple MD5 Zip Password Cracker
#Vicio - 2020

import zipfile
import time 

def main():
	try:
		Zip = raw_input("Enter Your Zip File Name: ")
		myZip = zipfile.ZipFile(Zip)
	except zipfile.BadZipfile:
		print "[!!!] There was an ERROR opening the zip file!"
		return

	password = ''

	start = time.time()
	pwdfile = raw_input("Please, enter your wordlist dictionary including the full path: ")
	try:
		f = open(pwdfile,"r")
	except:
		print "\nFile Not Found!"
		quit()
	passes = f.readlines()
	for pass_count, x in enumerate(passes):
		password = x.strip()
		try:
			myZip.extractall(pwd = password)
			end = time.time()
			t_time = end - start

			print "\nPassword Cracked: %s\n" % password
			print "It took --", t_time, "seconds to crack your password."
			print "\nThanks for crackin' with us :) "
			time.sleep(5)
			return
		except Exception as e:
			if str(e[0]) == 'Bad password for file':
				pass
			elif 'Error -3 while decompressing' in str(e[0]):
				pass
			else:
				print e
	print "Sorry, your password was not found."

if __name__ == '__main__':
 main()

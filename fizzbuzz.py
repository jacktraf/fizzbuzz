#!/usr/bin/env python
#
# Original task:
# 	Print numbers from 1-100
# 	If the number is a multiple of 3, print Fizz
# 	If the number is a multiple of 5, print Buzz
# 	But, if the number is a multiple of both, print fizzbuzz
#	So, to complete this task, it would be run like
#		fizzbuzz 3 5 0 100 1
# 
# Written using Arch Linux, havent tested it on other operating systems, so feedback is appreciated
# I will work on making it as cross-plateform as possible for the practice if nothing else..
# 
#

import sys
import os
from math import *

def main(fizz, buzz, startnumber, limit, increment):
	number = startnumber
	while (limit is None) or (number <= limit):
		if FizzBuzz(number, fizz, buzz) is True:
			print 'FizzBuzz'
		elif Fizz(number, fizz) is True:
			print 'Fizz'
		elif Buzz(number, buzz) is True:
			print 'Buzz'
		else:
			print number
		main(fizz, buzz, number + increment, limit, increment)
	exit(0)

def Fizz(n, fizz):
	if n % fizz == 0:
		return True
	else:
		return False

def Buzz(n, buzz):
	if n % buzz == 0:
		return True
	else:
		return False

def FizzBuzz(n, fizz, buzz):
	if ((Fizz(n, fizz) == True) and (Buzz(n, buzz) == True)):
		return True
	else:
		return False

if __name__ == '__main__':
	usage = """
		Usage: fizzbuzz.py FIZZ BUZZ STARTNUMBER LIMIT INCREMENT
	
		fizzbuzz.py starts counting from STARTNUMBER, incrementing by INCREMENT, until LIMIT is reached.
		fizzbuzz.py pritns 'Fizz' if that number is divisible by FIZZ, 'Buzz' if that number is divisable
		by BUZZ and 'FizzBuzz' if that number is divisible by both FIZZ and BUZZ.

		If an INCREMENT is not specified, it will be set to 1
				
		If LIMIT is not specified, program will continue to loop until user terminated (SIGINT / CTRL + C / ETC) 
	
		If STARTNUMBER is not specified, it will be set to 0
		"""

	NumOfArguments = len(sys.argv) - 1 
	if (NumOfArguments is 0) or (NumOfArguments is 1):
		print usage
		exit(1)
	elif NumOfArguments is 2:
		fizz         = int(sys.argv[1])
		buzz         = int(sys.argv[2])
		startnumber  = 0
		limit        = None
		increment    = 1
		main(fizz, buzz, startnumber, limit, increment)
	elif NumOfArguments is 3:
		fizz         = int(sys.argv[1])
		buzz         = int(sys.argv[2])
		startnumber  = int(sys.argv[3])
		limit        = None
		increment    = 1
		main(fizz, buzz, startnumber, limit, increment)
	elif NumOfArguments is 4:
		fizz         = int(sys.argv[1])
		buzz         = int(sys.argv[2])
		startnumber  = int(sys.argv[3])
		limit        = int(sys.argv[4])
		increment    = 1
		main(fizz, buzz, startnumber, limit, increment)
	elif NumOfArguments is 5:
		fizz         = int(sys.argv[1])
		buzz         = int(sys.argv[2])
		startnumber  = int(sys.argv[3])
		limit        = int(sys.argv[4])
		increment    = int(sys.argv[5])
		main(fizz, buzz, startnumber, limit, increment)
	else:
		print 'Error: Too many arguments'
		exit(1)

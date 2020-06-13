from random import randint
import sys

x=int(input('Enter start of the range: '))
y=int(input('Enter end of the range: '))

answer=randint(int(x),int(y))

while True:
	try:
		guess=int(input('guess a number from {n1} to {n2}: '.format(n1=x,n2=y)))
		if x < guess < y:
			if guess==answer:
				print('You are a genius!!!')
				break

		else:
			print('Hey friend,I said guess from {n1} to {n2}: '.format(n1=x,n2=y))
	except ValueError:
		print('Please enter a number')
		continue
				




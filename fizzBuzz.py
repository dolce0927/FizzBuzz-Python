"""Write a program that prints the numbers from 1 to 100. 
But for multiples of three print “Fizz” instead of the
number and for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five 
rint “FizzBuzz”."

 if number number is divisible by 3 and 5 then fizzbuzz
	else if number is divisible by 5 then buzz
	else if is divisible by 3 then fizz
	else if number is not divisible by 3 or 5 then return the number"""

	
for num in range(1, 100):
	if num % 3 == 0 and num % 5 == 0:
		print("FizzBuzz")
	elif num % 3 == 0:
		print("Fizz")
	elif num % 5 == 0:
		print("Buzz")
	else:
		print(num)

import time 
import math 

def calculate_time(func): 
	def inner1(*args, **kwargs): 
		begin = time.time() 
		func(*args, **kwargs) 
		end = time.time() 
		print("Total time taken in : ", func.__name__, end - begin) 

	return inner1 

@calculate_time
def factorial1(num): 
	time.sleep(2) 
	print(math.factorial(num)) 


def factorial2(num): 
	time.sleep(2) 
	print(math.factorial(num)) 

# sugar syntax!
factorial1(10)

# long way
calculate_time(factorial2(10))

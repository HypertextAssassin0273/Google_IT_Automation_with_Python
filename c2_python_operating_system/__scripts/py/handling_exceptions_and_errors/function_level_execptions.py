#!/usr/bin/env python3

def enhanced_read_and_divide(filename):
	try:
		data = None
		with open(filename, 'r') as file:
			data = file.readlines()
		
        # Ensure there are at least two lines in the file
		if len(data) < 2:
			raise ValueError("Not enough data in the file.")

		num1 = int(data[0]); num2 = int(data[1])
		
        # Check if second number is zero
		if num2 == 0:
			raise ZeroDivisionError("The denominator is zero.")

		return f'{num1}/{num2} = {num1 / num2}'
	
    # catch exceptions:
	except FileNotFoundError:
		return "Error: The file was not found."
	except ValueError as ve:
		return f"Value error: {ve}"
	except ZeroDivisionError as zde:
		return f"Division error: {zde}"

# test function:
if __name__ == "__main__":
    print(enhanced_read_and_divide("data.txt")) 							# FileNotFoundError
    print(enhanced_read_and_divide("../../__assets/div_inputs/case-1.txt")) # ValueError
    print(enhanced_read_and_divide("../../__assets/div_inputs/case-2.txt")) # ValueError
    print(enhanced_read_and_divide("../../__assets/div_inputs/case-3.txt")) # ZeroDivisionError
    print(enhanced_read_and_divide("../../__assets/div_inputs/case-4.txt")) # 10/2 = 5.0 [Success]

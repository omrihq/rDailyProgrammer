#Write a program that will take coordinates, and tell you the corresponding number in pascals triangle. For example:
#Input: 1, 1
#output:1
#=======
#input: 4, 2
#output: 6
#=======
#input: 1, 19
#output: error/nonexistent/whatever
import re 

def factorial(n):
	if n == 0:
		return 1
	else:
		fac = 1
		for i in xrange(1,n+1):
			fac*=i
	return fac

#If it is row 4, column 2, we want 4 choose 2
#The formula for this combination is (row!)/((row!)*(row-column)!)
#Also, remember that the first row/column in the triangle is row/column 0, not 1

def prompt():
	print "Hello, this will give you the number of a coordinate in pascals triangle"
	coordinates = raw_input("Enter the coordinates as follows (row, column) ")
	coordinates = re.findall('\d+', coordinates)
	return coordinates

def calculate_number(coordinates):
	row = int(coordinates[0])
	column = int(coordinates[1])
	pascals_number = (factorial(row)/((factorial(column))*factorial(row-column)))
	if pascals_number < 1:
		return -1
	return pascals_number

def main():
	coords = prompt()
	number = calculate_number(coords)
	if number > 0:
		print number
	else:
		print "Non-existant"

if __name__ == '__main__':
	main()
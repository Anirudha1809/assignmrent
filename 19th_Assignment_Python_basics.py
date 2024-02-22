#1.Declear two variables 'x' and 'y',and assign them integer values.swap the values of those variables without using any temporary variablr

x=int(10)
y=int(20)
x=x+y
y=x-y
x=x-y
print("the values of x:",x,"the value of y:",y)

'''2.create a program that the area of a rectangle.take the lenght and the width as input from the user and store them in variables
and calculate and display the area'''

length=float(input('Enter the length of the rectangle :'))
width=float(input('Enter the width of the rectangle :'))
area=length*width
print('The Area of the Rectangle is',area)


'''3.Write a program that converts temperature from celsis to Fahrenhit.take the tempareture in celsius as input and store it in a 
veriable,convert it to farhenheit and display it'''

temp_c=float(input('Enter temperature in Celsius : '))
temp_f=(9/5*(temp_c)+32)
print(f'Temperature in Fahrenheit = {temp_f}')


'''4.Write a Python program that takes a string as input and prints the length of
the string.'''
str = "Anirudha"
print(len(str))

'''Create a program that takes a sentence from the user and counts the number
of vowels (a, e, i, o, u) in the string.'''
def Check_Vow(string, vowels):
    final = [each for each in string if each in vowels]
    print(len(final))
    print(final)
     
string = "Anirudha"
vowels ="AaEeIiOoUu"
Check_Vow(string,vowels)

'''6.Given a string, reverse the order of characters using string slicing and print
the reversed string.'''

t_str = "Anifromcse"
print("The original string is : " + t_str)
K = 7
res = t_str[(K-1)::-1]
print("The reversed sliced string is : " + res)

'''7.Write a program that takes a string as input and checks if it is a palindrome
(reads the same forwards and backwards).'''

def isPalindrome(s):
	return s == s[::-1]
s = "Anirudha"
ans = isPalindrome(s)
if ans:
	print("Yes")
else:
	print("No")

'''8.Create a program that takes a string as input and removes all the spaces from
it. Print the modified string without spaces.'''

def removeSpaces(string):
	string = string.replace(' ','')
	return string
string = "a nirud ha gu pta "
print(removeSpaces(string))
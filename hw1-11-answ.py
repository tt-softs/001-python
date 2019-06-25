###  1. Define a function, that takes string as argument and prints `"Hello, %arg%!"`
#!/bin/python3.6
from string import Template

def	print_hello_arg(arg):
    print('"Hello, %{}%!"'.format(arg)) # 2 since ver 2.7

	
def	print_hello_arg_all(arg):
    print ('"Hello, %' + str(arg) + '%!"') # 0 bad 
    print('"Hello, %%%s%%!"' % arg) # 1 old style
    print('"Hello, %{}%!"'.format(arg)) # 2 since ver 2.7
    print(f'"Hello, %{arg}%!"') # 3 since ver 3.6
    t = Template('"Hello, %$name%!"')  # 4 use templates
    print(t.substitute(name=arg))

print_hello_arg("dev")
print_hello_arg(13)

###  2. Define a function `sum()` and a function `multiply()` that sums and multiplies (respectively) all the numbers 
### in a list of numbers. For example, `sum([1, 2, 3, 4])` should return 10, and `multiply([1, 2, 3, 4])` should return 24.

def sum(n): 
  total = 0 
  for i in n: 
    total += i
  return total 

def multiply(n): 
  total = 1 
  for i in n: 
    total *= i
  return total 

print( sum([1, 2, 3, 4]) )
print( multiply([1, 2, 3, 4]) )

### 3. Define a function `reverse()` that computes the reversal of a string. For example, `reverse("I am testing")` should return the string "gnitset ma I".

def reverse(string):
    return string[::-1]
	
print( reverse("I am testing") )


### 4. Define a function `isPalindrome()` that recognizes palindromes (i.e. words that look the same written backwards). 
### For example, `isPalindrome("radar")` should return True.



def isPalindromeSlow(string):
  return string == string[::-1]

def isPalindrome(string):
  for i in range(len(string)//2):
    if string[i] != string[-1-i]:
      return False
  return True
	
print( isPalindrome("I am testing") )
print( isPalindrome("radar") )
print( isPalindrome("арозаупаланалапуазора") )


### 5. Define a procedure `histogram()` that takes a list of integers and prints a histogram to the screen. 
### For example, `histogram([4, 9, 7])` should print the following:
import time

def histogram(arr):
    for i in arr:
        for j in range(i):
          time.sleep(1)
          print("", end="*", flush=True)
        print()


histogram([4, 9, 7])

### 6. Define a function `caesarCipher` that takes string and `key(number)`, whuch returns encrypted string

def caesarCipher(string, key):
    symbols = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for char in string:
      if char.isupper():
        result += symbols[(symbols.find(char.lower()) + key) % len(symbols)].upper()
      else:
        result += symbols[(symbols.find(char) + key) % len(symbols)]   
    return result

print(caesarCipher("abcxyzABCXYZ", 2))


### 7. define a function `diagonalReverse()` that takes matrix and returns diagonal-reversed one:

def diagonalReverse(lst):
    n = len(lst)
    m = len(lst[0])
    res = [[lst[j][i] for j in range(n)] for i in range(m)]
    return res

arr = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],]
print(diagonalReverse(arr))

### 8. Write a function `game()` number-guessing game, that takes 2 int parameters defining the range. Using some kind of `random` 
### function to generate random int from the range. While user input isn't equal that number, print "Try again!". If user guess the number, 
### congratulate him and exit.


import random

def game(start, end):
  rand = random.randint(start, end)
  while int(input("Guess int from {} to {} : ".format(start,end))) != rand:
    print("Try again!")
  
  return True


print(game(1, 10))

### 9. Define a function, which takes a string with N opening brackets `("[") and N closing brackets ("]")`, in some arbitrary order.
### Determine whether the generated string is balanced; that is, whether it consists entirely of pairs of opening/closing brackets (in that order), 
### none of which mis-nest.

def	checkBrackets(str):
	i = 0
	for char in str:
		if char == "[":
			i += 1
		elif char == "]":
			i -= 1
		if i < 0:
			break
	return "OK" if  i == 0  else "NOT OK" 
	
	
print(checkBrackets("[[]]"))
print(checkBrackets("[[][]]"))
print(checkBrackets("[][]"))

print(checkBrackets("["))
print(checkBrackets("][][ "))
print(checkBrackets("[]][[]"))

print(checkBrackets("[[[]]"))
print(checkBrackets("]]]]]"))
print(checkBrackets("[[[[["))

### 10. Write a function `charFreq()` that takes a string and builds a frequency listing of the characters contained in it. Represent the frequency 
### listing as a Python dictionary. Try it with something like `charFreq("abbabcbdbabdbdbabababcbcbab")`.

def charFreq(str):
	char_dict = {}
	for c in str:
		if c in char_dict:
			char_dict[c] += 1
		else:
			char_dict[c] = 1
	return char_dict
	
print(charFreq("abbabcbdbabdbdbabababcbcbab"))

### 11. Write a function `decToBin()` that taces decimal integer and outputs its binary representation.

def decToBin(i):
    return "{0:b}".format(i)
	
print(decToBin(8))


### 12. Write a ship battle game, which is similar to ex.8, except it takes 1 integer as an order of matrix, randomly generates index (x, y) and checks user input (2 integers).
### hard task: Visualize the game.
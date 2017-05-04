# Python: Basics

## Operators

### Math Operators
|Operator  |Operation  |Example  |Evaluates to..  |
|:--:|:--:|:--:|:--:|
| ** | Exponent | 2**3 | 8 |
| % | Modulus | 22%8 | 6 |
| // | Integer division | 22//8 | 2 |
| / | Division | 22/8 | 2.75 |
| * | Multiplication | 3*5 | 15 |
| - | Subtraction | 5-2 | 3 |
| + | Addition | 2+2 | 4 |

The order of operations is similar to the order used in mathematics.

> Note that when you perform division over two integers, even without using `//`, you get an integer division.

### Comparison Operators
| Operator | Meaning |
|:--|:--|
| == | Equal to |
| != | Not equal to |
| < | Less than |
| > | Greater than |
| <= | Less than or equal to |
| >= | Greater than or equal to |

### Boolean Operators
- `and`
- `or`
- `not`

### Augmented Assignment Operators

| Augmented assignment statement | Equivalent assignment statement |
|:--|:--|
| aVal += 1 | aVal = aVal + 1 |
| aVal -= 1 | aVal = aVal - 1 |
| aVal *= 1 | aVal = aVal * 1 |
| aVal /= 1 | aVal = aVal / 1 |
| aVal %= 1 | aVal = aVal % 1 |


## Data Types
| Data Type | Examples |
|:--|:--|
| Integers | -2, -1, 0, 1, 2, ... |
| Floating point numbers | -1.24, -1.0, --0.5, 0.0, 0.5, ... |
| Strings | 'a', 'aa', '', ... |
| Bool | True, False |
| Absence of a value (null, nil, undefined) | None |

Note that integers, floats, and strings are immutable.


## Input/Output

### Input
`input()` function waits for the user to type some text on the keyboard and press ENTER. If assigned to a variable, `input()` assigns keyboard input into the variable.
```python
userInput = input()
```

### Output
`print()` function displays the string value passed as argument.
```python
print('Hello world!')
```

`print()` without the parentheses also works.
```python
print 'Hello world!'
```


## Flow Control

### Conditional

#### `if` Statements
```python
if name == 'Alice':
	print('Hi, Alice')
elif name == 'Bob':
	print('Hi, Bob')
else:
	print('Hello')
```

### Looping

#### `while` Statements
```python
i = 0
while i < 5:
	print('run for five times')
	i += 1
```

**`break`**
Exits out of a loop

**`continue`**
Immediately jumps back to the start of the loop and reevaluates the loop's condition

> Some of the values (other than normal Boolean values) that could be evaluated True/False are:
False: `0`, `0.0`, `''`
True: All other values

#### `for` Loops
```python
for i in range(5):
	print('prints this five times')
```

**`range()`**
- With 1 argument: Starts from 0, increments by 1 up to the value passed as an argument, exclusive.
- With 2 arguments: Starts from the first value specified, increments up to the second value, exclusive.
	```python
	# Prints 12, 13, 14, 15
	for i in range(12, 16):
		print(i)
	```
- With 3 arguments: Starts from the first value passed as an argument, increments by the third value passed as an argument, up to the second value, exclusive.
	```python
	# Prints 5, 4, 3, 2, 1, 0
	for i in range(5, -1, -1):
		print(i)
	```

## Importing Modules

### `import`

```python
# Imports modules 
import random, sys, os, math
```

To use functions in the imported module, you have to start with the module name: 
```python
import random
random.random()
```

### `from`...`import`
```python
from random import *
```

This is same as `import random`, but allows you to use functions in the module without specifying which module the function is from:
```python
from random import *
random()
```


## Functions

### Basic Form
```python
# Prints 'Hello Alice'
def sayHello(name):
	print('Hello ' + name)
sayHello('Alice')
```

### Keyword Arguments
Most arguments are identified by their position in the function call. However, keyword arguments are identified by the keyword put before them in the function call. These are often used for optional parameters. 

For example, `print()` function has the optional parameters `end` and `sep` to specify what should be printed at the end of its arguments and between its arguments, respectively:
```python
# Prints `HelloWorld`, Removes /n at the end
print('Hello', end='')
print(`World`)

# Prints 'cats,dogs,mice' with ',' inserted between arguments
print('cats','dogs','mice',sep=',')
```


## Scopes

### Edge cases

#### Local and Global Variables with the Same Name
Local variable "shadows" the global variable with the same name

### `global` Statement
Lets you modify a global variable from within a function. The value remains modified even when the variable goes out of scope:
```python
# Prints 'spam'
def spam():
	global eggs
	eggs = 'spam'
	
eggs = 'global'
spam()
print(eggs)
```


## Exception Handling
**`try`**
Place the code that could potentially have an error.

**`except`**
Place the code that needs to run in case an error occurs.

```python
def division(value):
	try:
		return 42/value
	except ZeroDivisionError:
		print('Error occurred')

# Prints 'Error occurred'
division(0)
```


## Lists (~=Array)
A list is a value that contains multiple values in an ordered sequence. It is just like an array in other languages, except that in Python, a list can hold values of different data types:
```python
# All are valid
[1,2,3]
['hello', 3.14, True, 4]
```

Note that lists are mutable.

### Methods
**`index()`**
Checks if the value passed as an argument exists in the list: 
- If exists, returns the index of the value. 
- If not, then Python produces a `ValueError` error.

**`append()`**
Adds the argument to the end of the list.

**`insert()`**
Inserts a value at a specified index. The first argument is the index for the new value, and the second argument is the new value to be inserted.
```python
aList = ['one','three','four']
aList.insert(1, 'two')  # aList becomes ['one', 'two', 'three', 'four']
```

**`remove()`** 
Removes the value passed as an argument from the list
```python
aList = ['one', 'two', 'three']
aList.remove('two')  # aList becomes ['one', 'three']
```

**`sort()`**
Sorts the list in ascending order by default. To sort in descending order, pass `True` for `reverse` keyword argument:
```python
aList = [2,3,1,4]
aList.sort()  # [1,2,3,4]
aList.sort(reverse=True)  # [4,3,2,1]
```

> You cannot sort lists with both number values and string values in them. Also, note that `sort()` uses "ASCIIbetical order", not alphabetical order.

> If you need to sort the values in regular alphabetical order, pass `str.lower` for `key` keyword argument:
```python
alphabets = ['a','z','A','Z']
alphabets.sort(key=str.lower)  # ['a','A','z','Z']
```

Note that `sort()` sorts the items in-place. If you want a copy of the list sorted, use `sorted()` instead. 

### Tricks

#### Removing Values from a List
The `del` statement will delete values at an index in a list. All of the values in the list after the deleted value will be moved up one index:
```python
aList = ['one', 'two', 'three']
del aList[1]  # Removes 'two' from the list, now ['one', 'three']
```

#### Negative Indexes
The integer value -1 refers to the last index in a list, the value -2 refers to the second-to-last index in a list, and so on.
```python
aList = [1,2,3]
aList[-1]  # Returns 3
```

#### Sublists with Slices
A slice can get several values from a list, in the form of a new list. A slice is typed between square brackets, like an index, but it has two integers separated by a colon:
- The first integer is the index where the slice starts. 
- The second integer is the index where the slice ends. A slice goes up to, but will not include, the value at the second index.
[firstIndex: secondIndex)

You can leave out one or both of the indexes on either side of the colon in the slice:
- Leaving out the first index is the same as using 0
- Leaving out the second index is the same as using the length of the list

#### List Concatenation and List Replication
The `+` operator can combine two lists to create a new list. The `*` operator can also be used with a list and an integer value to replicate the list:
```python
[1,2,3] + ['A','B','C']  # Returns [1,2,3,'A','B','C']
[1,2,3] * 3  # Returns [1,2,3,1,2,3,1,2,3]
```

#### Determining a value is in a list
`in` and `not in` operators can be used to determine whether a value is or isn't in a list. 
```python
list = [1,2,3]
2 in list  # Evaluates to True
```

#### Multiple Assignment
You can assign multiple variables with the values in a list in a line of code: 
```python
# color = 'white', size = 24, name = 'Alice'
values = ['white', 24, 'Alice']
color, size, name = values
```

The number of variables and the length of the list must be exactly equal, or Python will give you a `ValueError`.

### Tuples
Tuples are just like lists, except that they are immutable and are wrapped with `()`, not `[]`. 

#### Converting Types
If you need to use lists and tuples interchangeably, use `list()` and `tuple()` to change types. 


## Dictionaries
A dictionary is a collection of many values in key-value pairs, typed with `{}`
```python
dict = {}
```

### Dictionaries vs Lists
Unlike lists, items in dictionaries are unordered. Therefore, they can't be sliced like lists. 

Trying to access a key that does not exist in a dictionary will result in a `KeyError` error message, much like `IndexError` for lists. If you assign a value to a dictionary with a key that does not exist, Python will add that value to the dictionary with the key.

### Methods

**`keys()`**
Returns a list of keys in a dictionary

**`values()`**
Returns a list of values in a dictionary

**`items()`**
Returns a list of tuples of keys and values in a dictionary

**`get()`**
Checks if the value passed as the first argument exists in the dictionary (checks for key), falls back to the second value if the key doesn't exist. 
```python
dict = {'one': 1, 'two': 2}
dict.get('three', 3)  # Since 'three' doesn't exist in dict, returns 3
```

Note that `get()` doesn't insert the fallback value into the dictionary.

**`setdefault()`**
Checks if the value passed as the first argument exists in the dictionary (checks for key), inserts the second value with the first value as a key if the first value doesn't exists. 

### Tricks

#### Determining a Key or Value Exists in a Dictionary
Use `in` or `not in` with `keys()` or `values()`. 


## Strings
Strings can begin and end with either single quotes or double quotes. 

### Methods
**`upper()`, `lower()`**
Turns all the characters inside the string to uppercase/lowercase characters.

**`isupper()`, `islower()`**
Returns True/False based on whether the string contains at least one uppercase/lowercase character inside it.

**`isalpha()`**
Returns True if the string consists only of letters and is not blank.

**`isalnum()`**
Returns True if the string consists only of letters and numbers and is not blank.

**`isdecimal()`**
Returns True if the string consists only of numeric characters and is not blank.

**`isspace()`**
Returns True if the string consists only of spaces, tabs, and new lines and is not blank

**`istitle()`**
Returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.

**`startswith()` `endswith()`**
Returns True if the string value they are called on begins or ends with the string passed to the method.

**`join()` **
Is called on a string, gets passed a list of strings, and returns a string. The returned string is the string with called-on-string in between each string in the list. 
```python
', '.join(['cats', 'bats', 'rats'])  # Returns 'cats, bats, rats'
```

**`split()`**
Is called on a string, by default, splits the string into a list of strings wherever whitespace characters are found. If a delimiter is passed as an argument, the function splits the string wherever the argument string is found. 

**`rjust()`, `ljust()`, `center()`**
Returns a padded version of the string they are called on, with spaces inserted to justify the text. If a second argument is given, they pad with the value given as the second argument, not with spaces.

**`strip()`, `rstrip()`, `lstrip()`**
`strip()` returns a new string without any whitespace characters at the beginning or end
`lstrip()`, `rstrip()` returns a new string with whitespace characters from left, right ends removed respectively.

If a string argument is passed, that string pattern will be stripped. 

### Raw Strings
To use raw strings, place an `r` before a string. A raw string completely ignores all escape characters. 
```python
print(r'That\'s mine')  # Prints "That\'s mine", not "That's mine"
```

### Multiline Strings
Begin and end with three single quotes or double quotes. Any new lines, tabs, or quotes in between the triple quotes are considered part of a string.

### Tricks

#### Concatenation
Strings can be concatenated with `+` operator.
```python
# Returns 'AliceBob'
'Alice' + 'Bob'
```

#### Replication
Strings can be replicated with `*` operator.
```python
# Returns 'AliceAliceAliceAliceAlice'
'Alice' * 5
```

#### Indexing and Slicing
Indexing strings returns characters at the specified index. Slicing works the way slicing works on lists. 

#### Working with Individual Characters
If you need to work with individual characters in a string (ex. changing a character), make it a list and turn it back to a string only when needed.
```python
st = 'someString'
li = list(st)    # ['s', 'o', 'm', 'e', 'S', 't', 'r', 'i', 'n', 'g']
li[5] = '5'
"".join(li)      #  'someS5ring'
```


## Value vs Reference
Python uses reference whenever variables must store values of mutable data types, such as lists or dictionaries. For values of immutable data types such as strings, integers, or tuples, Python variables will store the value itself.

When a function is called, the values of the arguments are copied to the parameter variables. For lists and dictionaries, a copy of reference is used for the parameter.

If you need to copy a list's values to another list, use `copy` module:
- `copy()` can be used to make a duplicate copy of a mutable value like a list or dictionary
- `deepcopy()` if the list you need to copy contains lists.  


## Useful Functions
`len()`
- If a string is passed as an argument, returns the number of characters in the string
- If a list is passed as an argument, returns the number of elements in the list

`str()`, `int()`, `float()`
- Evaluates the value passed in as an argument into another data type. 


## Reference
- Automate the Boring Stuff with Python Book
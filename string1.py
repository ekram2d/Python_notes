# The code snippet you provided is demonstrating how to include quotes inside a string in Python. It
# shows that you can use single quotes inside double quotes and vice versa without any issues. This
# allows you to include quotes within a string without causing syntax errors.
# Quotes Inside Quotes
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

# Example
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')



# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

# Example
# You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


# The strip() method removes any whitespace from the beginning or the end:

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
age = 36
txt = f"My name is John, I am {age}"
print(txt)
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# The split() method splits a string into a list.

# You can specify the separator, default separator is any whitespace.
txt = "welcome to the jungle"

x = txt.split()

print(x)

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)




# Example string for demonstration
txt = "  Hello, World!  "

# capitalize()
print(txt.capitalize())  # " hello, world!"

# casefold()
print(txt.casefold())  # "  hello, world!  "

# center()
print(txt.center(20, '-'))  # "---  Hello, World!  ---"

# count()
print(txt.count("o"))  # 2

# encode()
print(txt.encode())  # b'  Hello, World!  '

# endswith()
print(txt.endswith("!"))  # False

# expandtabs()
tabs_example = "H\te\tL\to"
print(tabs_example.expandtabs(4)) 
# expandtabs()
tabs_example = "H\te\tL\to"
print(tabs_example.expandtabs(4))  # "H   e   L   o"

# find()
print(txt.find("World"))  # 9

# format()
name, age = "John", 25
print("My name is {}, and I am {} years old.".format(name, age))  # My name is John, and I am 25 years old.

# index()
print(txt.index("World"))  # 9

# isalnum()
print("Hello123".isalnum())  # True

# isalpha()
print("Hello".isalpha())  # True

# isascii()
print(txt.isascii())  # True

# isdigit()
print("12345".isdigit())  # True

# isidentifier()
print("variable_name".isidentifier())  # True

# islower()
print("hello".islower())  # True

# isnumeric()
print("12345".isnumeric())  # True

# isspace()
print("   ".isspace())  # True

# istitle()
print("Hello World".istitle())  # True

# isupper()
print("HELLO".isupper())  # True

# join()
items = ["a", "b", "c"]
print("-".join(items))  # "a-b-c"

# ljust()
print("Hello".ljust(10, '-'))  # "Hello-----"

# lower()
print(txt.lower())  # "  hello, world!  "

# lstrip()
print(txt.lstrip())  # "Hello, World!  "

# partition()
print(txt.partition("World"))  # ('  Hello, ', 'World', '!  ')

# replace()
print(txt.replace("World", "Python"))  # "  Hello, Python!  "

# rfind()
print(txt.rfind("o"))  # 8

# rjust()
print("Hello".rjust(10, '-'))  # "-----Hello"

# rstrip()
print(txt.rstrip())  # "  Hello, World!"

# split()
print(txt.split())  # ['Hello,', 'World!']

# splitlines()
multi_line = "Hello\nWorld"
print(multi_line.splitlines())  # ['Hello', 'World']

# startswith()
print(txt.startswith("  H"))  # True

# strip()
print(txt.strip())  # "Hello, World!"

# swapcase()
print(txt.swapcase())  # "  hELLO, wORLD!  "

# title()
print(txt.title())  # "  Hello, World!  "

# upper()
print(txt.upper())  # "  HELLO, WORLD!  "

# zfill()
print("42".zfill(5))  # "00042"




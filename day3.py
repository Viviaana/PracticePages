#CHALLENGE 1
space1="O"
space2="O"
space3="O"
space4="X"
space5="X"
space6=" "
space7="O"
space8=" "
space9=" "

print("    |     |    ")
print("  {} |  {}  | {} ".format(space1, space2, space3))
print("    |     |    ")
print("---------------")
print("    |     |    ")
print("  {} |  {}  | {} ".format(space4, space5, space6))
print("    |     |    ")
print("---------------")
print("    |     |    ")
print("  {} |  {}  | {} ".format(space7, space8, space9))
print("    |     |    ")

if space1=="O" and space2=="O" and space3=="O":
    print("O wins!")
elif space1=="X" and space2=="X" and space3=="X":
    print("X wins!")
else:
    print("No winner")


#CHALLENGE 2

age=60

child_price="£8"
adult_price="£10.95"
senior_price="£7.50"

if age<18:
    print("The price of this ticket is {}".format(child_price))
elif age<60:
    print("The price of this ticket is {}".format(adult_price))
else:
    print("The price of this ticket is {}".format(senior_price))



def press_grind_beans():
    print("Grinding for 20 seconds")

press_grind_beans()



coffee_is_grinding = False

def press_grind_beans():
    if coffee_is_grinding:
        print("The coffee is grinding")
    else:
        print("The coffee is not grinding")

press_grind_beans()



def coffee_order(size, type_of_drink):
    print("Ordering a {} {}".format (size, type_of_drink))
    
coffee_order("tall", "mocha")



def add_up(num1, num2):
    return num1+num2

print(add_up(2,5))




def multiply_by_nine_fifths(celsius):
    return celsius * (9/5)

def get_fahrenheit(celsius):
    return multiply_by_nine_fifths(celsius) + 32

print("The temperature is {}°F".format(get_fahrenheit(19)))



#ACTIVITY 1

def take_order(topping1, topping2):
    print("Pizza with {} and {}".format(topping1, topping2))

take_order("Pineapple", "Ham")

#CHALLENGE 1

#ATTEMPT 1
def top_row(space1, space2, space3):
    print("    |     |    ")
    print("  {} |  {}  | {} ".format(space1, space2, space3))
    print("    |     |    ")
    print("---------------")
def middle_row(space4, space5, space6):
    print("    |     |    ")
    print("  {} |  {}  | {} ".format(space4, space5, space6))
    print("    |     |    ")
    print("---------------")
def bottom_row(space7, space8, space9):
    print("    |     |    ")
    print("  {} |  {}  | {} ".format(space7, space8, space9))
    print("    |     |    ")

top_row("x","x","o")
middle_row("x","o","x")
bottom_row("o", " ", " ")

def tic_tac_toe(space1, space2, space3, space4, space5, space6, space7, space8, space9):
    print("    |     |    ")
    print("  {} |  {}  | {} ".format(space1, space2, space3))
    print("    |     |    ")
    print("---------------")
    print("    |     |    ")
    print("  {} |  {}  | {} ".format(space4, space5, space6))
    print("    |     |    ")
    print("---------------")
    print("    |     |    ")
    print("  {} |  {}  | {} ".format(space7, space8, space9))
    print("    |     |    ")

tic_tac_toe("x","x","o","x","o","x", "o", " ", " ")


#CHALLENGE 2

def int_to_string(int1):
    return str(int1)

print("{} is a string now.".format(int_to_string(1)))

#Challenge 3

def add_one(num1):
    return num1+1

print(add_one(2))

#Challenge 4

def minus_one (num1):
    return num1-1

print(minus_one(1))

#CHALLENGE 5

def add_up (num1, num2):
    return num1 + num2

print(add_up(2, 2))

#CHALLENGE 6

def take_off (num1, num2):
    return num1 - num2

print(take_off(2, 2))

#CHALLENGE 7

def times_by (num1, num2):
    return num1 * num2

print(times_by(3, 2))

#CHALLENGE 8

def divide_by (num1, num2):
    return num1 / num2

print(divide_by(3, 2))

#CHALLENGE 9

def times_self (num1):
    return num1 * num1

print(times_self(3))

#CHALLENGE 10

def add_up (num1, num2):
    return num1 + num2
def take_off (num1, num2):
    return num1 - num2
def times_by (num1, num2):
    return num1 * num2
def divide_by (num1, num2):
    return num1 / num2

def final_sum(num1, num2, ops):
    if ops==("*"):
        print("{} {} {} = {}".format(num1, ops, num2, times_by(num1,num2)))
    elif ops==("+"):
        print("{} {} {} = {}".format(num1, ops, num2, add_up(num1,num2)))
    elif ops==("-"):
        print("{} {} {} = {}".format(num1, ops, num2, take_off(num1,num2)))
    elif ops==("/"):
        print("{} {} {} = {}".format(num1, ops, num2, divide_by(num1,num2)))
    else:
        print("Invalid input")

final_sum(2,5,"+")
final_sum(4,6,"*")
final_sum(8,6,"f")

#CHALLENGE 11

def higher(number1, number2):
    if number1 > number2:
        return("{} is higher than {}".format(number1,number2))
    elif number2 > number1:
        return("{} is higher than {}".format(number2,number1))
    else:
        return("The numbers are the same")

print(higher(2,3))
print(higher(6,5))
print(higher(3,3))


#CHALLENGE 12

def lower(number1, number2):
    if number1 < number2:
        return("{} is lower than {}".format(number1,number2))
    elif number2 < number1:
        return("{} is lower than {}".format(number2,number1))
    else:
        return("The numbers are the same")

print(lower(2,3))
print(lower(6,5))
print(lower(3,3))

#CHALLENGE 13

def equal(number1, number2):
    if number1 == number2:
        return("The numbers are equal")
    else:
        return("The numbers are not equal")

print(equal(2,3))
print(equal(3,3))

#CHALLENGE 14

def show_lower(number1, number2):
    if number1 < number2:
        return("{}".format(number1))
    elif number2 < number1:
        return("{}".format(number2))
    else:
        return("The numbers are the same")

print(show_lower(2,3))
print(show_lower(6,5))
print(show_lower(3,3))


#CHALLENGE 15

def show_higher(number1, number2):
    if number1 > number2:
        return("{}".format(number1))
    elif number2 > number1:
        return("{}".format(number2))
    else:
        return("The numbers are the same")

print(show_higher(2,3))
print(show_higher(6,5))
print(show_higher(3,3))

#CHALLENGE 16

def check_even(num1):
    return num1 %2

def is_even(num1):
    if check_even(num1) == 0:
        return("The number {} is even".format(num1))
    else:
        return("The number {} is not even".format(num1))
    
print(is_even(8))
print(is_even(9))

#CHALLENGE 17

def check_odd(num1):
    return num1 %2

def is_odd(num1):
    if check_even(num1) == 0:
        return("The number {} is not odd".format(num1))
    else:
        return("The number {} is odd".format(num1))
    
print(is_odd(8))
print(is_odd(9))

#CHALLENGE 18

def grading(grade):
    if grade >89 and grade<101:
        return("Grade A")
    elif grade >79 and grade <90:
        return("Grade B")
    elif grade >69 and grade <80:
        return("Grade C")
    elif grade >59 and grade <70:
        return("Grade D")
    else:
        return("Grade F")

print(grading(76))
print(grading(46))
print(grading (60))

#CHALLENGE 19

def concatenated(word1, word2):
    print("{}{}".format(word1, word2))

concatenated("hello", "world")

#CHALLENGE 20


def check_vowels(word):
    for vowel in 'uioae':
       word.count(vowel)
   return(vowel)

print(check_vowels("pizza"))

def count_vowels(word):
    num_vowels=0
    for vowel in word:
        if vowel in "aeiouAEIOU":
           num_vowels = num_vowels+1
    return num_vowels

print(count_vowels("cheese"))







coffee_order = [
    'Sam - Hot Chocolate',
    'Andrew - Flat White',
    'Ezra - Champagne']

coffee_order[2] = 'Ezra - Latte'
coffee_order.append("Stuart - Cortado")
coffee_order.pop()
print(coffee_order)

print(len(coffee_order))


#Activity 1

fave_webs = [
    "Reddit",
    "Cracked",
    "Facebook"]
bob_fave_webs = [
    "Metro",
    "BBC News",
    "Reddit"
    ]

fave_webs.extend(bob_fave_webs)
fave_webs.pop()
fave_webs.remove("Facebook")
fave_webs.reverse()
fave_webs.sort()
fave_webs.sort(reverse=True))
print(fave_webs.count("Reddit"))






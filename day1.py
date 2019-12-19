print('Hello, World')
print("My name is Katie")
print(30)
print(6.28)
print(None)
print(True)
This is how you add a comment that won't appear when you run
print(len('hello'))
print('hello'.upper())
print('hello'.capitalize())


#count example using  list
vowels = ['a', 'e', 'i', 'o', 'i', 'u'] #create the list
count = vowels.count('i') #identify the data that needs to be counted
print('The count of i is:', count)# print the number of that data shown in the list

#count example using strings
string = "hello, hello" 
print(string.count("hello", 0, 5)) #1 is mandatory, next 2 optional
print(string.count("hello", 0, 12)) #spaces and punctuation count for the optional data, ie 10 would still show 1 but 12 shows 2

#basic count example
print("hello".count("l"))

print("hello".find("e")) #position numbers always start at 0 so 2nd item is 1

print("hello".replace("e","a")) #first item is what to find, 2nd item is what to replace it with

print("hello"[4]) #shows the specific letter instead of data about it
print("hello"[2:4])

#random number generator
import random
print(random.randint(11,20))

#tic tac toe
print("   |   |   ")
print("   |   |   ")
print("   |   |   ")
print(" ---------")
print("   |   |   ")
print("   |   |   ")
print("   |   |   ")
print(" ---------")
print("   |   |   ")
print("   |   |   ")
print("   |   |   ")

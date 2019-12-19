print("All Around the World"[7].upper())

name="Katie"
age= 28
likes_cats= True

print(name)
print(age)
print(likes_cats)



my_num=10
print(my_num +5)
print(my_num -5)
print(my_num *5)
print(my_num /5)
print(my_num **5)
print(my_num %5)


my_num=10

my_num +=5
my_num = my_num +5 same thing, just a shorthand method

my_num **=5
my_num -=5
my_num /=5
print(my_num)



favourite_drink="tea"
#print("My favourite drink is "+ favourite_drink)
print ("My favourite drink is {}".format(favourite_drink))


Activity 1
name= "Katie"
age=28
favourite_colour="red"

print("My name is {}, I am {} years old and my favourite colour is {}".format(name, age, favourite_colour))

#Activity 2

breakfast="cereal"
lunch="a sandwich"
dinner="chicken"

print("Today I had {} for breakfast, {} for lunch and {} for dinner".format(breakfast, lunch, dinner))

breakfast="toast"
lunch="pie"
dinner="fish"

print("Tomorrow I will have {} for breakfast, {} for lunch and {} for dinner".format(breakfast, lunch, dinner))


#Activity 3

from datetime import date
f_date = date(2019, 12, 4)
l_date = date(2020, 5, 17)
delta = l_date - f_date
print(delta.days)

#Activity 4

space1="X"
space2="O"
space3=" "
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







age=27

if age==30:
    print("Yay, you are 30")
elif age==19:
    print("Not 19 forever")
elif age==21:
    print("You can now drink in America")
else:
    print("well that is a rubbish age")


age=18

if age>17:
   print("Yes I can serve you")
else:
   print("You aren't old enough!")


age=18
country="UK"

if age>17 and country=="UK":
    print("Yes I can serve you")
else:
    print("You aren't old enough!")







#CHALLENGE 1

password="viiew"

if len(password)>7:
    print(password)
else:
    print("Password is too short")



#CHALLENGE 2

num=11

remainder3= num %3
remainder5= num %5

if remainder3==0 or remainder5==0:
    print("This number is divisible by 3 or 5")
else:
    print("This number is not divisible by 3 or 5")



#CHALLENGE 3

num=15

remainder3= num %3
remainder5= num %5

if remainder3==0 and remainder5!=0:
    print("Fizz")
elif remainder3!=0 and remainder5==0:
    print("Buzz")
elif remainder3==0 and remainder5==0:
    print("Fizz Buzz")
else:
    print(num)


#CHALLENGE 4

num ="1234321"

revnum = num[::-1]

if num==revnum:
    print("This number is a palindrome")
else:
    print("This number is not a palindrome")


#CHALLENGE 5

time=11
place_of_work="Manchester"
town_of_home="Sale"

if time<8 or time>17:
    print("At {} I am at home in {}".format(time, town_of_home))

elif time==8:
    print("At {} I'm commuting to work in {}".format(time, place_of_work))

elif time==17:
    print("At {} I'm commuting home to {}".format(time, town_of_home))

elif time>8 or time<17:
    print("At {} I'm at work in {}".format(time, place_of_work))




#CHALLENGE 6

word="jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi"

def findLastIndex(word, x): 
    index = -1
    for i in range(0, len(word)): 
        if word[i] == x: 
            index = i 
    return index 
   
x = 'i'
  
index = findLastIndex(word, x) 
  
if index == -1: 
    print("Character not found") 
else: 
    print('Last index is', index) 


#CHALLENGE 7

word="bob"

if(word[0] == word[-1]):
    print("True")
else:
    print("False")



#CHALLENGE 8

num1=5
num2=4

total=num1+num2

even=total %2

if even==0:
    print(total)
else:
    print(num1*num2)














































    









#Write a program that tests the compatability between 2 people
#Take both people names and check for the number of times the letters in the word TRUE occurs, then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.
#for love scores less than 10 or greater than 90, the message should be: Your score is x, you go together like coke and mentos. 
#for love scores between 40 and 50, the message should be: Your score is x, you are alright together. 
name1 = input("Please enter your name: ")
name1 = name1.lower()
name2 = input("Please enter your crush's name: ")
name2 = name2.lower()

a='t'
b='r'
c='u'
d='e'
e='l'
f='o'
g='v'
h='e'

first = name1.count(a)
second = name1.count(b)
third = name1.count(c)
fourth = name1.count(d)
fifth = name2.count(a)
sixth = name2.count(b)
seventh = name2.count(c)
eighth = name2.count(d)

ninth = name1.count(e)
tenth = name1.count(f)
eleventh = name1.count(g)
twelfth = name1.count(h)
thirteenth = name2.count(e)
fourteenth = name2.count(f)
fifteenth = name2.count(g)
sixteenth = name2.count(h)

x = first + second + third + fourth + fifth + sixth + seventh + eighth
y = ninth + tenth + eleventh + twelfth + thirteenth + fourteenth + fifteenth + sixteenth

pre_final = x*10
final = pre_final+y


if(final<10 or final>90):
    print(f"Your score is {final}, you go together like coke and mentos.")
elif(final>40 and final<50):
    print(f"Your score is {final}, you are alright together")
else:
    print(f"You are an ordinary couple, your score is {final}")
#Write a program that prints each number from 1 to 100 in turn. When the number is divisible by 3, then instead of printing the number, it should print "Fizz".  When the number is divisible by 5, it should print "Buzz". When the number is divisible by both 3 and 5, it should print "FizzBuzz"

for i in range(1,101,1):
    #print(i)
    if i % 3 == 0 and i%5 != 0:
        print("Fizz")
    elif i % 5 == 0 and i%3 != 0:
        print("Buzz")
    elif i%3==0 and i%5 == 0:
        print("FizzBuzz")
    else:
        print(i)
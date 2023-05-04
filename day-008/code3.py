num = int(input("Please enter a number : "))

def check_prime(num):
    is_prime = True
    for i in range(2,num):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("This is not a prime number")

check_prime(num)
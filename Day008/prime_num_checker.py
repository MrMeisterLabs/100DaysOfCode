#Write your code below this line ๐

def prime_checker(number):
    if number % 2 != 0 and number % 3 != 0 :
        print(f"It's a prime number")
    else:
        print(f"It's not a prime number")

#Write your code above this line ๐
    
#Do NOT change any of the code below๐
n = int(input("Check this number: "))
prime_checker(number=n)
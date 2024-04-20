#Coded By DarkZ143
print("Select one option to perform action : ")
print("Prime Number = 1")
print("Fibonacci series = 2")
print("Factorial = 3")
print("Reverse of Number = 4")
print("Pyramid = 5")
print("Character count = 6")
print("Check Even or Odd = 7")
number = int(input("Select Option : "))
#Function for Checking Prime Number...
if number == 1:
    def check_prime(n):
        if n>1:
            for i in range(2,(n//2)+1):
                if (n%i)==0:
                    print(n,"is not prime")
                    break
            else:
                print(n,"is prime")
        else:
            print(n,"is not prime")            
    
    n = int(input("Enter a number: "))
    check_prime(n) 

#Function for Fibonacci Series...
if number == 2 :
    def fibonacci(n):
        fib_series = [0, 1]
        while fib_series[-1] < n:
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series[:-1]
    n = int(input("Enter Number : "))
    print("Fibonacci series of ",n," is : ",fibonacci(n))

#Function for Factorial...
if number == 3 :
    
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    n = int(input("Enter a number: "))
    print("Factorial of ",n," is : ", factorial(n))

#Function for Reverse of the Number...
if number == 4 :
    def reverse(n):
        rev = 0
        while n>0:
            digit = n%10
            n = n//10
            rev = rev * 10 + digit
        print("Reverse = ", + rev)    
    n = int(input("Enter number :"))
    reverse(n)

#Function for Print Pyramid...
if number == 5 :
    def print_pyramid(n):
        for i in range(n):
            print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    n = int(input("Enter a number : "))
    print_pyramid(n)

#Function for string count
if number == 6 :
    def count_characters(input_string):
        return len(input_string)

    # Test the function
    input_string = str(input("Enter String : "))
    print("Number of characters:", count_characters(input_string))

#function for checking given number is Even or Odd...
if number == 7:
    def Even_Odd(n):
        if n % 2 == 0:
            print(n,"is Even")
        else:
            print(n,"is Odd") 
    n = int(input("Enter Number : ")) 
    Even_Odd(n)       
        

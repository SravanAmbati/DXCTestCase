x=''

def fibonacci(n):
    a = 0
    b = 1
    # check if input is not a negative number or zero
    if n <= 0:
        print("Please enter a positive number")

    # Checks and do actual operation if input is positive number     
    elif n>0:
        # This for loop gives the Fibonacci series 
        for i in range(0, n):
            print(a)
            c = a + b
            a = b
            b = c
            sum=b-1
        print (f"And the sum of series is {sum}")

    else:
        print("Please enter a valid positive Integer")

# This loop is to run to program continuously until we give exit
#If we give exit as input Program will stop
while x != "exit":
    x= input("Enter a number:")
    # try except block is used to avoid unexpected errors 
    try:
        x = int(x)
        #This calls the fibonacci function and prints output
        fibonacci(x)
    except:
        print("Given Input is string, Please Enter a Number")
    
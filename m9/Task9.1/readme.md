### Module 9 Python Essentials
#### TASK 9.1 

 1. The function was developed as indicated in the assignment.

 ![](Screenshots/1.png)
 
 ```python
 
 def get_reply(number):
    if number%5==0 and number%3==0:
        return 'FizzBuzz'
    elif number%3==0:
        return 'Fizz'
    elif number%5==0:
        return 'Buzz'
    else:
        return ''
        
 ```
 
 2. FizzBizz test developed.
 
 ![](Screenshots/2.png)
 
 ```python
 
 import fizz_buzz

def test_fizz(number):
    result = fizz_buzz.get_reply(number)

    if result == "Fizz":
        print("Test Fizz     number = ", number, "Complete");
    else:
        print("Test Fizz     number = ", number, "Incomplete");



def test_buzz(number):
    result = fizz_buzz.get_reply(number)

    if result == "Buzz":
        print("Test Buzz     number = ", number, "Complete");
    else:
        print("Test Buzz     number = ", number, "Incomplete");



def test_fizzbuzz(number):
    result = fizz_buzz.get_reply(number)

    if result == "FizzBuzz":
        print("Test FizzBuzz number = ", number, "Complete");
    else:
        print("Test FizzBuzz number = ", number, "Incomplete");


for number in range(1, 101):

    test_fizz(number)

    test_buzz(number)

    test_fizzbuzz(number)


 ```
 
 3. Result of test.
  
 ![](Screenshots/3.png)
 
 ![](Screenshots/4.png)
  
 
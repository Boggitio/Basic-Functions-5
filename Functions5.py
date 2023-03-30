#21 This function calculates the distance between two points on an xy axis. The position of the points are asked as
# input. The result is returned.
import math

def distance_between_points(x1, x2, y1, y2):
    #x1 = float(input("Enter the x-coordinate of the first point: "))
    #y1 = float(input("Enter the y-coordinate of the first point: "))
    #x2 = float(input("Enter the x-coordinate of the second point: "))
    #y2 = float(input("Enter the y-coordinate of the second point: "))

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    #return distance

    return(f"The distance between the points is: {distance}")

#22 - This function asks for a word and finds which letter is the most common one in it and returns that letter and
# the amount of times it is encountered.
def most_frequent_letter(s):
    s = s.lower()
    freq = {}
    for c in s:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    most_frequent = None
    most_frequent_count = 0
    for c in freq:
        if freq[c] > most_frequent_count:
            most_frequent = c
            most_frequent_count = freq[c]

    return(f"The most frequent letter in '{s}' is '{most_frequent}', which appears {most_frequent_count} times.")
#most_frequent_letter(input("Specify a word to count the most common letter in it:  "))

#23 - This function finds the sum of a chosen amount of the first natural numbers and returns the result.
def sum_of_naturals(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

#n = int(input("Enter the amount of the first natural numbers you want the sum of:  "))
#result = sum
    #return(f"The sum of the first {n} natural numbers is: {sum}")


#24 - This function asks for a number and then adds each digit until the result is made of only one digit and returns
# the result.
def sumdigto1(x):
    #x = int(input("Write here the number you would like to find out the sum of it's digits:   "))
    digitsum = 0
    while x > 0:
        digit = x % 10
        digitsum += digit
        x //= 10

    while digitsum > 9:
        temp = digitsum
        digitsum = 0
        while temp > 0:
            digit = temp % 10
            digitsum += digit
            temp //= 10
    return digitsum

#print(f"The sum of all digits reduced to one digit is:  {sumdigto1()}")

#25 - This function asks for a chosen amount of the first natural numbers, finds their squares and then adds them up and
# returns the result.
def sum_of_squares(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum

#n = int(input("Specify how many of the first natural numbers' squares you want to know the sum of: "))
#print(f"The sum is: {sum_of_squares(n)}")
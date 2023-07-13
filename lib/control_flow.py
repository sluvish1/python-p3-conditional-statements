#!/usr/bin/env python3

def admin_login(username, password):
    if ((username == "admin" or username == "ADMIN") and password == "12345"):
        return "Access granted"
    else:
        return "Access denied"


def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif (temperature >= 40 and temperature <= 65):
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"


def fizzbuzz(num):
    if (num % 3 == 0 and num % 5 == 0):
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


def calculator(operation, num1, num2):
    dict_map = {
        "+": num1 + num2,
        "-": num1 - num2,
        "*": num1 * num2,
        "/": num1/num2
    }
    results = dict_map.get(operation,"Invalid operation!") 
    if results == "Invalid operation!":
        print("Invalid operation!")
        return None
    return results
        
    #if the operation is invalid print out Invalid operation and return None
    #.get goes though the dic_map and looks for the operator the user calls for,
    #  if that operator isnt listed itll return "invalid operation"
    #results value would be based upon the opertor if valid itll equal value but if invalid itll equal "invalid operation"
    #return dict_map[operation]


calculator("+", 1, 2)
# match operation:
#     case "+":
#         return num1+num2
#     case "-":
#         return num1-num2
#     case "*":
#         return num1*num2
#     case "/":
#         return num1/num2

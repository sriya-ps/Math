import random

maximum_length = 10
maximum_tokens = 9
minimum_tokens = 3
maximum_coefficient = 999999
minimum_coefficient = 100000

def get_secret():
    flag = True
    while flag:
        secret_input = input("Enter your secret integer (maximum length is " + str(maximum_length) + ") - ")
        if len(secret_input) > maximum_length:
            print("The secret is too long. Please enter your secret again.")
        else:
            try:
                global secret
                secret = abs(int(secret_input))
                flag = False
            except:
                print("The secret needs to be an integer. Please enter your secret again.")

def get_total_tokens():
    flag = True
    while flag:
        total_tokens_input = input("Enter the number of tokens to be generated (maximum is " + str(maximum_tokens) + ") - ")
        try:
            global total_tokens
            total_tokens = abs(int(total_tokens_input))
            if total_tokens > maximum_tokens:
                print("There are too many tokens. Please enter the number of tokens again.")
            elif total_tokens < minimum_tokens:
                print("There are too less tokens. Please enter the number of tokens again.")
            else:
                flag = False
        except:
            print("The number of tokens needs to be an integer. Please enter the number of tokens again.")

def get_quorum_tokens():
    flag = True
    while flag:
        quorum_tokens_input = input("Enter the number of quorum tokens (minimum is " + str(minimum_tokens) + ", maximum is " + str(total_tokens) + ") - ")
        try:
            global quorum_tokens
            quorum_tokens = abs(int(quorum_tokens_input))
            if quorum_tokens > total_tokens:
                print("There are too many quorum tokens. Please enter the number of quorum tokens again.")
            elif quorum_tokens < minimum_tokens:
                print("There are too less quorum tokens. Please enter the number of quorum tokens again.")
            else:
                flag = False
        except:
            print("The number of quorum tokens needs to be an integer. Please enter the number of tokens again.")
            
def generate_tokens():
    global coefficients, person_token
    coefficients = [secret]
    person_token = []
    for i in range(1, quorum_tokens):
        coefficients.append(random.randint(minimum_coefficient, maximum_coefficient))
    for i in range(1, total_tokens + 1):
        person_token.append([i, evaluate_token(i)])
        
def evaluate_token(person):
    token = 0
    for i in range(0, len(coefficients)):
        token += coefficients[i] * (person**i)
    return token

def print_tokens():
    print("----------------------------")
    print("   Person  |     Token      ")
    print("----------------------------")
    for i in person_token:
        print(" "*5 + str(i[0]) + " "*10 + str(i[1]))
    print("----------------------------")


get_secret()
get_total_tokens()
get_quorum_tokens()
generate_tokens()
print_tokens()
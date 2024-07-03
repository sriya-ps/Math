def get_quorum_tokens():
    flag = True
    while flag:
        quorum_tokens_input = input("Enter the number of quorum tokens - ")
        try:
            global quorum_tokens
            quorum_tokens = abs(int(quorum_tokens_input))
            flag = False
        except:
            print("The number of quorum tokens needs to be an integer. Please enter the number of tokens again.")

def get_tokens():
    global person_token
    person_token = []
    for i in range(quorum_tokens):
        flag = True
        while flag:
            identity_input = input("Enter the identity number #" + str(i+1) + " - ")
            try:
                person_token.append([abs(int(identity_input))])
                flag = False
            except:
                print("The identity number needs to be an integer. Please enter the identity number again.")
    for i in range(quorum_tokens):
        flag = True
        while flag:
            token_input = input("Enter the token number for identity " + str(person_token[i][0]) + " - ")
            try:
                person_token[i].append(abs(int(token_input)))
                flag = False
            except:
                print("The token number needs to be an integer. Please enter the token number again.")
               
def find_secret():
    global secret
    secret = 0
    for i in person_token:
        lagrange_value = 1
        x = 0
        for j in person_token:
            if j[0]!=i[0]:
                lagrange_value *= (x-j[0])/(i[0]-j[0])
        secret += lagrange_value * i[1]
    print("The secret has been retrieved. If incorrect, quorum is not met -", abs(round(secret))) 

get_quorum_tokens()
get_tokens()
find_secret()
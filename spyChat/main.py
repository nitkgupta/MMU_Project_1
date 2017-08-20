from spy_details import spy
from start_chat import  start_chat

print "Let's get started!"
question = "Do you want to continue as " + spy['salutation'] + " " + spy['name'] + " (Y/N): "
existing = raw_input(question)

# validating users input
if (existing.upper() == "Y") :
    # user wants to continue as default user.

    # concatination of salutation and name of spy.
    spy['name'] = spy['salutation'] + " " + spy['name']

    # starting chat application.
    start_chat(spy['name'], spy['age'], spy['rating'], spy['is_online'])
elif (existing.upper() == "N"):
    # user wants to continue as new user
    spy['name'] = raw_input("Provide your name here :")
    # chek wether spy has input something or not
    if len(spy['name']) > 0:
        spy['salutation'] = raw_input("What should we all you ? : ")

        while True:
            try:
                # converting users input to integer (typecasting)
                spy['age'] = int(raw_input("Enter your age. ?"))
                break
            except ValueError:
                print "Invalid age. Try again."

        # concatination of salutation and name of spy.
        spy['name'] = spy['salutation'] + " " + spy['name']

        while True:
            try:
                # converting users input to float (typecasting)
                spy['rating'] = float(
                    raw_input("What is your spy rating?"))
                break
            except ValueError:
                print "Invalid rating. Try again."
        spy['is_online'] = True

        # starting chat application.
        start_chat(spy['name'], spy['age'], spy['rating'], spy['is_online'])
    else:
        print "Invalid name. Try again."
else:
    print "Wrong choice. Try again."
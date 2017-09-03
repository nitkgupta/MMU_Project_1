from spy_details import spy
from start_chat import  start_chat
import re
print "Let's get started!"
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N): "
existing = raw_input(question)

if (existing.upper() == "Y") :

    spy.name = spy.salutation + " " + spy.name

    #Starting_chat
    start_chat(spy.name, spy.age, spy.rating, spy.is_online)
elif (existing.upper() == "N"):
    spy.name = raw_input("Provide your name here :")
    pattern1='^[a-zA-Z]+$'
    if(re.match(pattern1,spy.name)!=None):
        if len(spy.name) > 0:
            spy.salutation = raw_input("What should we call you ? : ")

            while True:
                try:
                    spy.age = int(raw_input("Enter your age. ?"))
                    break
                except ValueError:
                    print "Invalid age. Try again."

        spy.name = spy.salutation + " " + spy.name

        while True:
            try:
                spy.rating = float(
                    raw_input("What is your spy rating?"))
                break
            except ValueError:
                print "Invalid rating. Try again."
        spy.is_online = True

        start_chat(spy.name, spy.age, spy.rating, spy.is_online)
    else:
        print "Invalid name. Try again."
else:
    print "Wrong choice. Try again."
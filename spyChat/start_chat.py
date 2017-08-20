from add_status import add_status
from add_friend import add_friend
from select_friend import select_friend

def start_chat(name, age, rating, status):
    from globals import current_status_message

    if not (age > 12 and age < 50) :
        error_message = "Invalid age. Provide correct details."
        print error_message
    else:
        welcome_message = "Authentication complete. Welcome\n Name : " + name + "\nAge: " + str(age) + "\nRating: " + str(rating) + "\nProud to have you onboard"
        print welcome_message

        show_menu = True
        while show_menu:
            menu_choices = "What do you want to do? \n " \
                           "1. Add a status update \n " \
                           "2. Add a friend \n " \
                           "3. Send a secret message \n " \
                           "4. Read a secret message \n " \
                           "5. Read Chats from a user \n " \
                           "6. Close Application \n"
            result = int(raw_input(menu_choices))

            if (result == 1):
                current_status_message = add_status(current_status_message)
            elif (result == 2):
                number_of_friends = add_friend()
                print 'You have %d friends' % (number_of_friends)
            elif (result == 3):
                select_friend()
            elif (result == 6):
                show_menu = False
            else:
                print "wrong choice try again."
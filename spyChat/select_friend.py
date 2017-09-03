from spy_details import friends

def select_friend():
    # print the list of all friends.
    counter = 1
    for friend in friends:
        print str(counter) + ". " + friend.salutation + " " + friend.name
        counter += 1

    user_input = int(raw_input("Choose the friend from the list : "))
    if user_input <= counter:
        return user_input - 1
    else:
        print "Invalid choice. Try again"
        exit(-1)

from globals import STATUS_MESSAGES

updated_status_message = None

def add_status(current_status_message):
    if current_status_message != None:
        print 'Your current status message is %s \n' % (current_status_message)
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?:\n")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message
            print 'Your updated status message is: %s' % (updated_status_message)
        else:
            print "You did not provided any status message. Try again."
    elif default.upper() == 'Y':
        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages \n"))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]
            print 'Your updated status message is: %s' % (updated_status_message)
        else:
            print "Invalid choice. Try again."
    else:
        print 'The option you chose is not valid! Press either y or n.'

    return updated_status_message
from datetime import datetime
from select_friend import select_friend
from steganography.steganography import Steganography
def send_message():
    friend_choice= select_friend()
    original_image=raw_input("Enter the name of image in which message has to be hidden")
    pattern = '^[a-zA-Z]+\.jpg$'
    if (re.match(pattern, original_image) != None):
        output_image = raw_input("Enter the name of output image :")
        text = raw_input("Enter your message")
        Steganography.encode(original_image, output_image, text)
        new_chat={"message":text,"time":datetime.now(),"sent_by_me":True }
        friend[friend_choice]['chats'].append(new_chat)
        print 'Your secret message is ready'
    else:
        print "Invalid image name. try .jpg images only."



from datetime import datetime
from select_friend import select_friend
from steganography.steganography import Steganography
def read_message():
    sender=select_friend()
    secret_image = raw_input("Enter encrypted image :")
    secret_text=Steganography.decode(secret_image)
    new_chat={"message":secret_text,"time":datetime.now(),"sent_by_me":False}
    friend[sender]['chats'].append(new_chat)
    print 'Your secret message has been saved'
from select_friend import select_friend
from steganography.steganography import Steganography
def read_message:
    sender=select_friend()
    secret_image = raw_input("Enter encrypted image :")
    secret_text=Steganography.decode(secret_image)
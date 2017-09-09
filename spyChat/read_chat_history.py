from spy_details import friends
from select_friend import select_friend
def read_chat_history():
  read_for = select_friend()
  for chat in friends[read_for].chats:
      if chat.sent_by_me:
          print '[%s] %s %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
      else:
          print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)

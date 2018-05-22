from datetime import datetime
from termcolor import colored
import csv
#++++++++++++++++++++++++++++++++++++++++++++



#####Creating a class to maintain records of a spy
class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name= name
        self.salutation = salutation
        self.age= age
        self.rating= rating
        self.is_online=True
        self.chats=[]
        self.current_status_message= None

spy_1 = Spy('Mehta','Mr.', 21, 4.7)   # define spy_name, age, rating

###class to maintain records of the chat-messages from all sides
class ChatMessage:

  def __init__(self,spy_name,friend_name,time, message):
    self.spy_name = spy_name
    self.friend_name = friend_name
    self.message = message
    self.time = datetime.now()

friends = []  #list of friends
chats = []    #list of chats
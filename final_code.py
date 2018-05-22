from spy_details import spy_1 , Spy , friends , ChatMessage , chats
from datetime import datetime
import csv
from steganography.steganography import Steganography  #######stegnography fxn ---to receive and send a secret message and class-- when we got captical letter
from datetime import datetime                  ####datetime package
from termcolor import colored
#***********************************************************************


#######Application Start#########
print('Hello ')                                                 ## message print ##
print('What\s up')
print 'Lets started'

######### (2nd functoin start) declared that is updation(status)#########
def add_status(current_status_message):
    updated_status_message = None                      ###initially current status will be None

    if current_status_message != None:
        print "Your current status message is " + current_status_message + "\n"
    else:
        print 'You don\'t have any status message currently \n'
    default = raw_input("Do you want to select from older status (Y/N)? ")
    ##status_messages = ['My name is Mohit, I am Python Developer', 'Nice To Meet You']

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set?")

        if len(new_status_message) > 0:

            updated_status_message = new_status_message

            print("Your updated status is " + updated_status_message)

            STATUS_MESSAGES.append(updated_status_message)   ##appending newly entered status in the list

    elif default.upper() == 'Y':
        item_position = 1
        for message in STATUS_MESSAGES:                              ###use of for loop in the list
            print(str(item_position) + ' .' +  str(message))                ####  (*imp point)  next line
            item_position = item_position + 1

        message_selection = int(input("\nChoose from the above messages "))
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]    ##new status message will be updated

            print("Your updated status is " + updated_status_message)        ##print the updated mess.

    return updated_status_message                   ##stored the message

STATUS_MESSAGES = ['My name is Mohit, I am Python Developer', 'Nice To Meet You']   ####already stored the message

########add loading the function####################
def load_friends():

    with open('friends.csv', 'r') as friends_data:
        reader = csv.reader(friends_data)

    for row in reader:
        spy = Spy(name=row[0], salutation=row[1], rating=float(row[2]),age=int(row[3]))
        friends.append(spy)


##########(3rd function start) i.e. add friend  ############
def add_friend():
#taking the input from the user
    name = raw_input("Please add your friend's name: ")
    salutation = raw_input("Are they Mr. or Ms.?: ")
    name = salutation + ' ' + name
    age = int(raw_input('Age?'))
    rating = float(raw_input('Spy rating?'))

    if len('name') > 0 and age > 12 and rating >= 0:

        new_friend = Spy(name=name, salutation=salutation, age=age, rating=rating)  ###Class Spy used
        friends.append(new_friend)                             #add friend in new friend list

        with open('friends.csv','a') as friends_data:  #create or already a csv file and add friends details
            writer = csv.writer(friends_data)
            writer.writerow([new_friend.name, new_friend.salutation, new_friend.age,new_friend.rating,new_friend.is_online])
            #writerow keyword basically write the details
        print('Friends added')
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'
    return len(friends)

##########function to select a friend from spy friend list###########
def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s, Age is %d with Rating %.2f is online' % (item_number + 1, friend.name, friend.age , friend.rating)
        #like 1.mohit 2.eshant  3.rahul

        item_number = item_number + 1

    friend_choice = int(raw_input('Choose from your friends(enter Index No.)'))
    friend_choice_position = friend_choice - 1

    return friend_choice_position

#++++++++++++++++++++++++++++++++++++++++++++++++
special_words = ['SAVE ME', 'SOS' , 'HELP']
#+++++++++++++++++++++++++++++++++++++++++++++++++

########(4th function start) send secret message ########
def send_message():

    friend_choice = friends[select_a_friend()].name

    original_image = raw_input("What is the name of the image?")
    output_path = 'output.jpg'                    #Auto. create a new file and store the secret message in this file
    text = raw_input("What do you want to say?")
    if text in special_words:
        text = colored(text + ": IT'S EMMERGENCY!! Come for help", "red")

    Steganography.encode(original_image, output_path, text)   #encoding process
    new_chat = ChatMessage(spy_name=spy_1.name, friend_name=friend_choice, time=datetime.now().strftime("%d %B %Y"),message=text)
    #link to spy_details file

    chats.append(new_chat)  ##append the chat to the friends list

    print "Your secret message is ready!"

    with open('chats.csv','a') as chats_data:                  ## *{imp point)Auto. created and message will saved
        writer= csv.writer(chats_data)
        writer.writerow([new_chat.spy_name, new_chat.friend_name, new_chat.time, new_chat.message])

########(5th Function Start) read a secret message ########
def read_message():
    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")           #enter the new file name
    secret_text = Steganography.decode(output_path)             #decoding process
    #show a text message in the new file
    print(secret_text)

    chat = ChatMessage(spy_name=spy_1.name, friend_name=sender, time=datetime.now().strftime("%d %B %Y"), message=secret_text)

    friends[sender].chats.append(chat)             #appending the chat
    print "Your secret message has been saved!"

    with open('chats.csv','a') as chats_data:           ## *{imp point}Auto. created and message will saved
        writer=csv.writer(chats_data)
        writer.writerow([chat.spy_name, chat.friend_name,chat.time,chat.message])   #sender -jise aaya hai message

#######(6th function Start) Read chat that user entered##########
def readchat(choice):
    name_friend = friends[choice].name
    with open('Chats.csv', 'rU') as chats_data:
        reader = csv.reader(chats_data)
        for row in reader:
            try:
                c = ChatMessage(spy_name=row[0], friend_name=row[1], time=row[2], message=row[3])
                # checking the chats of the current spy with selected friend
                if c.spy_name == spy_1.name and c.friend_name == name_friend:
                    print colored("You sent message to the Spy name: %s "%name_friend,"red")
                    print colored("On Time: [%s]"%c.time,"blue")
                    print("Message: %s"% c.message)
                    return 1
            except IndexError:
                pass
            continue

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from datetime import datetime
time= datetime.now()
print('Time is:'+'' + str(time))
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

###(1st function Calling) i.e. start functoin
def start_chat(spy_name, spy_age, spy_rating):
    show_menu = True
    current_status_message = None  #Initially, current status set to none

    def load_friends():
        with open('friends.csv', 'rU') as friends_data:
            reader = csv.reader(friends_data)
            for row in reader:
                try:
                    friends.append(Spy(name=row[0], salutation=(row[1]), age=int(row[2]), rating=float(row[3])))
                except IndexError:
                    pass
                continue

    # load_chats() is a function which loads all the chats of spies stored in chats.csv
    def load_chats():
        with open("chats.csv", 'rU') as chat_data:
            reader = csv.reader(chat_data)
            for row in reader:
                try:
                    chats.append(ChatMessage(spy_name=row[0], friend_name=row[1], time=row[2], message=row[3]))
                except IndexError:
                    pass
                continue

    # both functions are called so that chats and list of friends are loaded before its usage
    load_friends()
    load_chats()
#+++++++++++++++++++++++++++++++++++++++++++

    while show_menu==True:
        #conditions
        menu_choices = "What do you want to do? \n 1.Add a status update\n 2.Add a friend\n 3.Show Friends\n 4.Send a secret Message\n" \
                       " 5.Read a secret Message\n 6.Read chats from a user\n 7.Close a program\n"
        menu_choice = int(raw_input(menu_choices))

        if (menu_choice == 1):
            print('You choose to update the status ')
            current_status_message = add_status(current_status_message)        # Add Status Update

        elif menu_choice == 2:
            number_of_friends = add_friend()
            print('You have %d friends\n' %(number_of_friends))            ##printing number of friends spy has

        elif menu_choice == 3:
            select_a_friend()

        elif menu_choice == 4:
            send_message()

        elif menu_choice==5:
            read_message()

        elif menu_choice == 6:
            print("Reading chat from user")
            print "Select a friend whose chat you want to see"
            choice = select_a_friend()
            readchat(choice)

        elif menu_choice == 7:
            show_menu = False
            print("Close the application")                        #Exit Application

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
question = "Do you want to continue as default user (Y/N)?"

existing = raw_input(question)
if existing == "Y":

    print(" Welcome " + spy_1.salutation + " " + spy_1.name)    ##used Spy_details file
    start_chat(spy_1.name, spy_1.age, spy_1.rating)

else:
    print("Welcome to spychat application")

    spy_name = raw_input("Tell me your spy name first: ")
    if len(spy_name) > 3:

        spy_salutation = raw_input("What Should I call you Mr. or Ms.?: ")

        spy_name = spy_salutation + ' ' + spy_name

        print('Alright ' + spy_name + ' I would like to know a little bit more about you...')

        spy_age = raw_input("What is your age?")

        if spy_age < 12 or spy_age > 50:
            print("Sorry! your age is invalid to be a spy")
        else:
            spy_experience = raw_input("For how many years you are working as a spy ?")
            ##asking spy for his/her experience

            spy_rating = float(raw_input("What is your rating [out of 5]"))
            ##asking spy for his/her experience
            if spy_rating >= 4.5:
                print("Good Ace")
            elif spy_rating < 4.5 and spy_rating >= 3.5:
                ##else if statement
                print("You are one of the good ones")
            elif spy_rating < 3.5 and spy_rating >= 2.5:
                print ("You can do better")
            else:
                print("You can always take help of someone in the office")

            print("Thanks for providing information about yourself")
            print("Authentication complete!\nProud to have you on board \n " + spy_name + " of " + str(
                spy_age) + " years with a experience of " + spy_experience + " years and a rating of " + str(
                spy_rating))

        spy_1.is_online = True

        start_chat(spy_name, spy_age, spy_rating)
    else:
        print 'Invalid I/f,Again filled the  correct informaation'
##############################calling of start_chat function############################

                   ################Thank you #############





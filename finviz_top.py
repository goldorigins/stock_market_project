#this code takes a URL input and a class identifier
#input. these orders are sent to the other object
#to go and retrieve required table.

def user_input():
    user_info = [] #makes list to contain user inputs
    url_input = str(input('Input the URL (exactly as written) where table is located: '))
    user_info.append(url_input)#adds URL to list
    class_input = str(input('Input the class ID w/o spaces or quotes: '))
    user_info.append(class_input)#adds table id to list
    user1 = user_info
    return user1


    


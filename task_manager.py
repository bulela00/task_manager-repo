#=====importing libraries===========
from datetime import date

#=====Functions=====
#This functions receives a line of the task information and splits it into the pieces of task information.
#The task information is then printed line by line
def  print_task_info(task_info):
    task_info = task_info.strip()
    task_info = task_info.split(", ")
    print(f"Task: \t{task_info[1]}")
    print(f"Assigned to: \t{task_info[0]}")
    print(f"Date assigned: \t{task_info[3]}")
    print(f"Due date: \t{task_info[4]}")
    print(f"Task Complete? \t{task_info[5]}")
    print(f"Task description: \t{task_info[2]} \n")
    return 


#====Login Section====
#This code block will allow a user to login.   
with open('user.txt', 'r', encoding='utf-8-sig') as usersfile:    #The usernames and passwords are read from user.txt 
    usernames = []
    passwords = {}
    for line in usersfile:
        temp = line.strip()
        temp = temp.split(", ")
        usernames.append(temp[0])    #The usernames from the file are saved in a list of usernames                            
        passwords[temp[0]] = temp[1]    #Passwords are stored in the dictionary in username: password pairs

user_valid = False
user = input("Please enter your username: ")    #Requests username from user
while user_valid == False:        
      if user in passwords:    #Check if the username is one of the known usernames
           user_valid = True
      else:
           user_valid = False
           user = input("You have entered an invalid username. Please try again: ")

password = input("Please enter your password: ")    #Requests password from the user
password_valid = False
while password_valid == False:
      if password == passwords[user]:    #Check if the password corresponds to the username
            print("Login successful\n") 
            password_valid = True
      else:
            password = input("You have entered an invalid password. Please try again: ")


while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    if user == "admin": 
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
s - statistics                     
: ''').lower()
    else:
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()
         

    if menu == 'r':
        #This code block will add a new user to the user.txt file 
        if user == "admin":   
            new_user = input("Enter new username: ")    # Requests new username

            unique_user = False 
            while unique_user == False: 
                if new_user in passwords:    #Check if the username is already part of the users file.
                    new_user = input("Username already exists. Please enter a new username: ") 
                else:
                    unique_user == True
                    break 
                            
            password_confirmed = False
            while password_confirmed == False:
                new_password = input("Enter new password: ")    #Requests input of new password
                confirm_password = input("Confirm password: ")    #Request of password confirmation
                if confirm_password == new_password:
                    reg_info = new_user + ", " + new_password
                    with open('user.txt','a') as userfile:     #Writing new username and password to user.txt file
                        userfile.write("\n" + reg_info)
                    
                    print("New user registered.")
                    password_confirmed = True
                    break
                else:
                    print("Password incorrect.")   #Message indicating that the password and the confirmation don't match
        else: 
             print("Only the admin user is allowed to register new users\n")
             break                
            
    elif menu == 'a':
        #This code block will allow a user to add a new task to task.txt file
        user_ = input("Enter the username of the person whom the task is assisgned to: ")
        task_title = input("Enter the title of the task: ")
        task_description = input("Enter the description of the task: ")
        due_date = input("Enter the due date of the task: ")
        todays_date = date.today()    
        current_date = todays_date.strftime("%d %b %Y")   #Formatting the current date
        task_ = ", ".join([user_, task_title, task_description,current_date, due_date, "No" ])
        with open('tasks.txt','a') as taskfile:
             taskfile.write("\n" + task_)    #Writing the task information to the tasks.txt
        
        
    elif menu == 'va':
    #This code block will read the task from task.txt file and  
        with open('tasks.txt', 'r', encoding='utf-8-sig') as tasklines:
             for line in tasklines:
                  print_task_info(line)    #The function called will print out the task information of the given line

    elif menu == 'vm':
        pass
        #This code block will read the task from task.txt file and
        #print to the console in the format of Output 2 presented in the PDF
        with open('tasks.txt', 'r', encoding='utf-8-sig') as tasks:
             for line in tasks:
                  temptask = line.strip()
                  temptask = temptask.split(", ")
                  task_user = temptask[0]    #Extract the user that the current task is assigned to
                  if task_user == user:   #Check if the user the task is assigned to is the current user
                       print_task_info(line)   #Print task information if it is assigned to the current user
                  else:
                       pass
                          

    elif menu == 'e':
        print('Goodbye!!!')
        exit()


    elif menu == 's':
         if user == "admin":
              with open('user.txt', 'r', encoding='utf-8-sig') as all_users:
                   user_cnt = 0
                   for line in all_users:
                        user_cnt += 1

              with open('tasks.txt', 'r', encoding='utf-8-sig') as all_tasks:
                   task_cnt = 0
                   for line in all_tasks:
                        task_cnt += 1
                
              print(f"Total number of users: \t{user_cnt}\n")
              print(f"Total number of tasks: \t{task_cnt}\n")
         else:
              print("This option is only available to the admin user")


    else:
        print("You have entered an invalid input. Please try again")
# This bit of code opens a file for reading and creates a dictionary.
credentials_file = open('user.txt', 'r')
checklist = credentials_file.readlines()
credentials_file.close()
user_pass_Dict = {}
# This bit of code loops through the file.
for line in checklist:
    chop = line.split(",")
    clear = chop[1].strip().lower()
    username = chop[0]
    password = clear
    user_pass_Dict[username] = password
# This bit of code validates username and password in the file.
loop_count = 0
while(loop_count == 0):
    username_login = input("Please enter your username:")
    password_login = input("Please enter your password:")

    if(username_login in user_pass_Dict):
        if(user_pass_Dict[username_login] == password_login):
            loop_count = 1

        else:
            print("Incorrect password. Try again.")
            loop_count = 0

    else:
        print("Incorrect username. Try again.")
        loop_count = 0

while True:
        if username_login == "admin":
            admin_menu_str = str('''Select one of the following Options below:\n''' +
                         '''r - Registering a user\n''' +
                         '''a - Adding a task\n''' +
                         '''va - View all tasks\n''' +
                         '''vm - view my task\n''' +
                         '''ds - display statistics\n''' +
                         '''e - Exit\n''' +
                         ''': ''')
        else:
            admin_menu_str = str('''Select one of the following Options below:\n''' +
                         '''a - Adding a task\n''' +
                         '''va - View all tasks\n''' +
                         '''vm - view my task\n''' +
                         '''e - Exit\n''' +
                         ''': ''')

        menu = input(admin_menu_str).lower()


        if menu == 'r' and username_login == "admin":
            pass
            # Username must be followed by a comma and space.
            new_username = input("Enter a new username: ").lower()
            new_password = input("Enter a new password: ").lower()
            confirmation_password = input("Confirm password: ").lower()
            # A file is open and a condition is met to verify the password.
            with open('user.txt', 'a') as user_document:
                if new_password == confirmation_password:
                    user_document.write("\n")
                    user_document.write( new_username + "," + " " + new_password)
                else:
                        print("Incorrect confirmation password: ", confirmation_password)
            user_document.close()

        elif menu == 'a':
            pass
            # This bit of code requests user tasks and must be written followed by a comma and space.
            task_username = input("Username of the person whom the task is assigned to: ").lower()
            task_title = input("Title of the task: ").lower()
            task_description = input("Description of the task: ").lower()
            task_due_date = input("Task due date: ").lower()
            task_current_date = input("Current date: ").lower()
            # A file is opened and writes the task information.
            with open('tasks.txt', 'a') as task_document:
                task_document.write("\n" + task_username + ", " + task_title + ", " + task_description + ", " + task_due_date + ", " + task_current_date + ", " + "No")
                task_document.close()

        elif menu == 'va':
            pass
            # This bit of code opens a file for read and creates list variables.
            file = open('tasks.txt', 'r+', encoding='utf-8')
            username_register = []
            title_register = []
            description_register = []
            due_date_register = []
            current_date_register = []
            task_status_register = []
            task = []
            # This bit of code loops over lines inside a file.
            for line in file:
                chop = line.split(",")
                task.append(chop)

            for title in task:
                    print("Task: \t\t", "  ", title[1]) 
                    print("Assigned to: \t", title[0])
                    print("Date assigned: ", title[3])
                    print("Due date: \t", "  ", title[4])
                    print("Task complete? ", title[5])
                    print("Task description: \n", title[2])
            file.close()


        elif menu == 'vm':
            pass
            file = open('tasks.txt', 'r+', encoding='utf-8')
            task = []
            # This bit of code loops over lines inside file.
            for line in file:
                chop = line.split(",")
                task.append(chop)
            # This bit of code loops over a list and prints out only the login user tasks.
            for title in task:
                if username_login == title[0]:
                    print("Task: \t\t", "  ", title[1])
                    print("Assigned to: \t", title[0])
                    print("Date assigned: ", title[3])
                    print("Due date: \t", "  ", title[4])
                    print("Task complete? ", title[5])
                    print("Task description: \n", title[2])

            file.close()

        elif menu == 'ds' and username_login == "admin":
            # print total number of users and total number of tasks in a friendly format.
            # count number of lines in user.txt
            with open('user.txt', 'r') as user_document:
                user_count = len(user_document.readlines())
                print("\nTotal number of users: ", user_count)
            user_document.close()
            # count number of lines in tasks.txt
            with open('tasks.txt', 'r') as task_document:
                task_count = len(task_document.readlines())
                print("Total number of tasks: ", task_count)
            task_document.close()
            print ("\n")

        
        elif menu == 'e':
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")
    # Code ends here.
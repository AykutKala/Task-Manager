# Importing required functions for getting the date and comparing two dates.
from datetime import datetime

# Login Section
users_names = []
users_password = []
tasks = []
is_valid_user = False
user_selection = ""
username = ""


# Save task into the list and file
# This function is for adding new tasks
def save_task(new_task):
    tasks.append(new_task)

    with open('tasks.txt', 'a', encoding='utf-8') as write_tasks:
        write_tasks.write(f"{new_task}\n")

    print("New task is saved successfully!\n")


# Save user into the lists and file
# This function is for adding new users
def save_user(new_username, new_password):
    users_names.append(new_username)
    users_password.append(new_password)

    with open('user.txt', 'a', encoding='utf-8') as write_user:
        write_user.write(f"{new_username}, "
                         f"{new_password}\n")

    print("New user is saved successfully!\n")


# Loading existing users from user.txt
# This function is for reading users one by one
def load_users():
    with open('user.txt', 'r', encoding='utf-8') as read_user:
        for user in read_user:
            user = user.replace(",", "")
            user = user.strip("\n")
            user = user.split(" ")
            users_names.append(user[0])
            users_password.append(user[1])


# Loading existing tasks from tasks.txt
# This function is for reading for tasks
def load_tasks():
    with open('tasks.txt', 'r', encoding='utf-8') as read_tasks:
        for task in read_tasks:
            task = task.strip("\n")
            tasks.append(task)


# Check if entered user exists
# This function is for login usernames and passwords
def user_exists(user_name, user_password):
    result = False

    if user_name in users_names:
        user_index = users_names.index(user_name)
        if user_password == users_password[user_index]:
            result = True
        else:
            print("User is not found, please try again!")
    else:
        print("User is not found, please try again!")

    return result


# option "a"
# This function is for adding new tasks and their properties
def add_task():
    print("Please enter task details:")

    task_username = input("Username: ")
    task_title = input("Title: ")
    task_description = input("Description: ")

    # This loop is for checking due date and converting correct date
    due_date_is_correct = False
    task_due_date = datetime.today()
    while not due_date_is_correct:
        try:
            due_date_entry = input("Due date(dd/mm/yyyy): ")
            due_date_fields = due_date_entry.split("/")
            task_due_date = datetime(int(due_date_fields[2]), int(due_date_fields[1]), int(due_date_fields[0]))
            due_date_is_correct = True
        except:
            print("Invalid due date! please enter a valid due date!\n")

    task_completed = "No"
    # We need strftime to convert from int format to str format
    new_task = f"{task_username}, {task_title}, {task_description}, {datetime.today().strftime('%d %b %Y')}, " \
               f"{task_due_date.strftime('%d %b %Y')}, {task_completed}"
    save_task(new_task)


# This function is for viewing all tasks seperatly
def view_all_tasks():
    for task in tasks:
        task = task.split(", ")

        print(f"Assigned to:\t{task[0]}\nTask title:\t{task[1]}\n"
              f"Task description:\t{task[2]}\nAssigned date:\t{task[3]}\n"
              f"Due date:\t{task[4]}\nTask completed:\t{task[5]}\n")


# This function display only user's tasks
def view_my_tasks():
    for task in tasks:
        task = task.split(", ")
        if username == task[0]:
            print(f"Assigned to:\t{task[0]}\nTask title:\t{task[1]}\n"
                  f"Task description:\t{task[2]}\nAssigned date:\t{task[3]}\n"
                  f"Due date:\t{task[4]}\nTask completed:\t{task[5]}\n")


# This function is for register new users and checking duplicate username
def register_user():
    new_user_defined = False
    while not new_user_defined:
        new_username = input("Please enter the new username: ")
        new_password = input("Please enter the new password: ")
        confirm_new_password = input("Please confirm the new password: ")

        if new_username in users_names:
            # We do not allow admin to register same name users
            print("This username already exists, please choose another one!")
        else:
            if new_password != confirm_new_password:
                print("Passwords do not match, please try again!")
            else:
                new_user_defined = True
                save_user(new_username, new_password)


# These functions are for display tasks and users statistics
def display_tasks_statistics():
    all_tasks = len(tasks)
    # prepare display output for statistics:
    print(f"The total number of tasks: {all_tasks}")


def display_statistics():
    all_users = len(users_names)
    print(f"Total number of users:{all_users}")
    display_tasks_statistics()


# This function is for  user selections menu
def check_user_selection(users_selection):
    print("")
    if users_selection == "a":
        add_task()
    elif users_selection == "va":
        view_all_tasks()
    elif users_selection == "vm":
        view_my_tasks()
    elif users_selection == "e":
        exit()
    elif users_selection == "r" and username == "admin":
        register_user()
    elif users_selection == "ds" and username == "admin":
        display_statistics()
    else:
        print("Invalid entry!\n")


# Application runs from this point
# Login info
load_users()

while not is_valid_user:
    username = input("Please enter username: ")
    password = input("Please enter password: ")
    is_valid_user = user_exists(username, password)

print('Welcome ')
print("")
load_tasks()

# Show menu options
# Only admin menu
while username == "admin":
    user_selection = input("Please select one of the following options:\n"
                           "r - register user\na - add task\nva - view all tasks\nvm -"
                           " view my tasks\nds - display statistics"
                           "\ne - exit\nPlease select from the above options: ").lower()
    check_user_selection(user_selection)
# User's menu,not admin
while username != "admin":
    user_selection = input("Please select one of the following options:\n"
                           "a - add task\nva - view all tasks\nvm -"
                           " view my tasks\ne - exit\nPlease select from the above "
                           "options: ").lower()
    check_user_selection(user_selection)

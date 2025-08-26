import time

def get_input():
    """Read a file and return the list of to-do items"""
    user_text = input("Type add, show, edit, complete or exit: ")
    user_text = user_text.strip().lower()
    return user_text


def read_todos():
    """Write the to-do items list in the text file"""
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
        return todos


def write_todos(task):
    with open('todos.txt', 'w') as file:
        file.writelines(task)

def get_time():
    now = time.strftime("%b %d, %H:%M:%S")
    print("It is ",now)

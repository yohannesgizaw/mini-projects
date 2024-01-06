# a todo list program in python
import sys, datetime
tasks = []

#a fuunction to add tasks :

def add_task():
    task = input("Enter the task to add : ")
    tasks.append(task)
    print("task added succesfully !!")

#a function to print task:
    
def print_task():
    for index , value in enumerate(tasks,start=1):
        print(index, value)

#a function to remove a task:
        
def remove_task():
    num = int(input("Enter the task number to remove : "))
    for index,value in enumerate(tasks,start=1):
        if num == index:
            tasks.remove(value)
            print("Task removed successfully")
            break
        else :
            return "task not found"

# a function to show the menu :
        
while True:
    print("*******************TO DO LIST **************************")
    print("1.Add Task ")
    print("2.Show Tasks ")
    print("3.remove Task ")
    print("4.exit ")
    print("__________________________________________________________")
    choice = int(input("Enter an option : "))
    if choice == 1:
        add_task()
    elif choice == 2:
        print_task()
    elif choice == 3:
        remove_task()
    elif choice == 4:
        break
    else :
        print("Enter a valid choice : ")

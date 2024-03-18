#/bin/python3

from classes.managers import Manager
from classes.employees import Employee

def employee(name,email,manager_id):
    employee = Employee(name,email,int(manager_id))
    employee.save()
    print(f"{name} has been added")

def manager(name,email):
    manager = Manager(name,email)
    manager.save()
    print(f"{name} has been added")

def main():
    options = """
1. Add employee to the company
2. Add manager to the company
3. Exit program
"""
    print(options)
    option = input('Option >>> ')
    if option == '1':
        name = input('Enter employee\'s name: ')
        email = input('Enter employee\'s email: ')
        manager_id = input('Enter employee\'s manager id: ')
        employee(name,email,manager_id)
    elif option == '2':
        name = input("Enter manager\'s name: ")
        email = input("Enter manager\'s email: ")
        manager(name,email)
    elif option == '3':
        exit()
    else:
        print('Invalid Option')
    main()    

if __name__ == '__main__':
    main()

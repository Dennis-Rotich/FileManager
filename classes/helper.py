import os
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

def delete(file):
    if os.path.exists(f'/home/dennisrotich/Development/code/Mod3/Week4/FileManager/classes/files/{file}.txt'):
        os.remove(f'/home/dennisrotich/Development/code/Mod3/Week4/FileManager/classes/files/{file}.txt')
        print(f"{file} has been deleted.")
    else:
        print('File does not exist')

def overwrite(file,content):
    with open(f'/home/dennisrotich/Development/code/Mod3/Week4/FileManager/classes/files/{file}.txt',"w",encoding="utf-8") as f:
        f.write(content)
    print(open(f'/home/dennisrotich/Development/code/Mod3/Week4/FileManager/classes/files/{file}.txt', encoding='utf-8').read())
    print('Complete')

def write(file,content):
    with open(f'/home/dennisrotich/Development/code/Mod3/Week4/FileManager/classes/files/{file}.txt','a',encoding='utf-8') as f:
        f.write(content)
    print(open(f'/home/dennisrotich/Development/code/Mod3/Week4/FileManager/classes/files/{file}.txt', encoding='utf-8').read())    
    print('Complete')
    pass

def read(file):
    with open(f'/home/dennisrotich/Development/code/Mod3/Week4/FileManager/classes/files/{file}.txt',encoding='utf-8') as f:
        for line in f:
            print(line)
    print('Complete')

def create(file):
    with open(f'/home/dennisrotich/Development/code/Mod3/Week4/FileManager/classes/files/{file}.txt','x',encoding='utf-8') as f:
        pass
    print(open(f'/home/dennisrotich/Development/code/Mod3/Week4/FileManager/classes/files/{file}.txt', encoding='utf-8').read())

def assign():
    options = """
1. Add employee to the company
2. Add manager to the company
3. Go back
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
        home()
    else:
        print('Invalid Option')
    assign()

def employee_portal(name,employee_options):
    print(f"""

logged in as {name}
    """)
    print(employee_options)
    option = input('Option >> ')
    if option == '1':
        file = input('Enter file name: ')
        create(file)
    elif option == '2':
        file = input('Enter file name: ')
        content = input('Enter your content here: ')
        write(file, content)
    elif option == '3':
        file = file = input('Enter file name: ')
        read(file)
    elif option == '4':
        home()        
    else:
        print('Invalid option')
    employee_portal(name,employee_options)

def manager_portal(name,manager_options):
    print(f"""

logged in as {name}
    """)
    print(manager_options)
    option = input('Option >> ')
    if option == '1':
        file = input('Enter file name: ')
        create(file)
        pass
    elif option == '2':
        file = file = input('Enter file name: ')
        read(file)            
        pass
    elif option == '3':
        file = input('Enter file name: ')
        content = input('Enter your content here: ')
        write(file, content)            
        pass
    elif option == '4':
        file = input('Enter file name: ')
        content = input('Enter your content here: ')
        overwrite(file,content)            
        pass
    elif option == '5':
        file = input('Enter file name: ')
        delete(file)            
        pass
    elif option == '6':
        home()
        pass
    else:
            print('Invalid option')
    manager_portal(name,manager_options)

def files():
    employee_options = """
1. Create a file    
2. Write a file
3. Read a file
4. Go back
"""
    manager_options = """
1. Create a file
2. Read a file
3. Write a file
4. Overwrite a file
5. Delete a file
6. Go back
"""
    access = None
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    role = input('Enter your role: ')

    if role.capitalize() == 'Employee':
        employee = Employee.find_by_email(email)
        access = employee.username if employee else None

    elif role.capitalize() == 'Manager':
        manager = Manager.find_by_email(email)
        access = manager.username if manager else None

    if access == None:
        print('User not found! You have to be assigned first.\n')
        assign()
    elif access == 'user':
       employee_portal(name,employee_options)
       pass
    elif access == 'admin':
        manager_portal(name,manager_options)   

def home():
    options = """
1. Assign employees and managers
2. Go to files
3. Exit program
    """
    print(options)
    option = input('Option >>> ')
    if option == '1':
        assign()
    elif option == '2':
        files()
    elif option == '3':
        exit()
    else:
        print('Invalid option')
    home()                
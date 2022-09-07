##################################################################
# Author: Farhan Tahmid (fxt190006)
# Date: 9/6/2022
# File: assignment1_fxt190006.py
##################################################################

import sys, re, os, pickle

# Function for sysarg
def process_lines(personals):
    # Checking sysarg
    if len(sys.argv) < 2:
        print('Please enter a filename as a system arg')
        quit()

    #  Read the file
    f = open(os.path.join(os.getcwd(), (sys.argv[1])), 'r')
    
    # Remove the heading line of the CSV file
    line = f.readline()  

    while True:
        line = f.readline().strip()
        if not line:
            break
        
        # Split on comma to get the fields as text variables and modify last_name name and first_name name to be in uppercase
        temporary_list = line.split(',')  
        temporary_list[0] = temporary_list[0].capitalize()
        temporary_list[1] = temporary_list[1].capitalize()

        # Modify middle initial to be a single upper case letter. Use X as a middle initial in case one is missing
        if len(temporary_list[2]) != 1:
            temporary_list[2] = 'X'

        # Modify phone_number number w/ regex, in need
        while re.match('\w{3}-\w{3}-\w{4}', temporary_list[4]) is None:
            print('Phone ', temporary_list[4], ' is invalid')
            print('Enter phone_number number in form 123-456-7890')
            temporary_list[4] = input('Enter phone number: ')
            
        # Modify id_number w/ regex, in need
        while re.match('[A-Za-z][A-Za-z]\d{4}', temporary_list[3]) is None:
            print('ID invalid: ', temporary_list[3])
            print('ID is two letters followed by 4 digits')
            temporary_list[3] = input('Please enter a valid id number: ')

        # Create a Person object and save the object to a dictionary of personals, where id_number is the key.
        person = Person(temporary_list[0], temporary_list[1], temporary_list[2].capitalize(), temporary_list[3], temporary_list[4])
        personals[temporary_list[3]] = person

    # Return the dictionary of personals to main
    return personals


# Define a class called Person with fields last_name, first_name, middle_name, id_number, and phone_number
class Person:
    def __init__(personal, last_name, first_name, middle_name, id_number, phone_number):
        personal.last_name = last_name
        personal.first_name = first_name
        personal.middle_name = middle_name
        personal.id_number = id_number
        personal.phone_number = phone_number

    # Create a display() method to output fields as shown in the sample run
    def display(personal):
        print('Employee id_number: ', personal.id_number)
        print('\t', personal.first_name, ' ', personal.middle_name, ' ', personal.last_name)
        print('\t', personal.phone_number, '\n')


# Main function
if __name__ == '__main__':
    
    employees = {}
    employees = process_lines(employees)

    # Save the dictionary as a pickle file
    pickle.dump(employees, open('emp_pickle', 'wb'))
    
    # Open the pickle file for reading
    employees_pickle_file = pickle.load(open('emp_pickle', 'rb'))
    
    # Print each person using the Person display() method to verifiy if unpickled
    print('\nEmployee list:\n')
    
    for employee_id in employees_pickle_file.keys():
        employees_pickle_file[employee_id].display()
                
import os
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename= "Logs.txt",
                    format='%(levelname)s - %(name)s - "%(message)s" - %(asctime)s',
                    datefmt='%m/%d/%Y %H:%M:%S %p',
                    filemode='w')

from app.students_data import *
from app.validation import get_number, get_full_name
from app.grade_calculation import *
from app.data_files_usage import *

students_data_list = []

############################################### ask import students data manually of from file
while True:
    file_prompt = input("Do you want to provide students list manually? (yes/no): ").lower().strip()
    logging.info(f"Do you want to provide students list manually? (yes/no): User's answer: [{file_prompt}]")
    if file_prompt == 'yes':
    ############################################ ask to input student's name, username
        students_amount = get_number(user_input="How many students do you have? ",
                                            error_msg="Please enter a numeric value.")
        logging.info(f"How many students do you have? [{students_amount}]")
        student_count = 0
        while student_count < students_amount:
            another = input("Add a new student? (yes/no): ").lower().strip()
            logging.info(f"Add a new student? (yes/no). Answer from user: [{another}]")
            if another == 'yes':
                student_count += 1
                ########################################################### call student full name
                student_full_name = get_full_name(name=input("What is student's name? ").strip().title(),
                                             surname=input("What is student's surname? ").strip().title())
                logging.debug(f"Inputted Student's full name from user: [{student_full_name}]")
                ########################################################### call student age
                student_age = get_student_age(student_full_name)
                logging.debug(f"Inputted student's age from user: [{student_age}]")
                ########################################################## call students email
                student_email = get_email(student_full_name)
                logging.debug(f"Student email: [{student_email}]")
                ########################################################## call students grades
                this_year_grade = get_this_year_grade()
                logging.debug(f"Student's This year grade: [{this_year_grade}]")
                last_year_grade = get_last_year_grade()
                logging.debug(f"Student's Last year grade: [{last_year_grade}]")
                average_grade = get_average_grade(student_full_name, this_year_grade, last_year_grade)
                logging.debug(f"Student's Average Grade: [{average_grade}]")
                ######################################################### store student data in a dictionary
                personal_data = {
                    "name": student_full_name,
                    "age": student_age,
                    "email": student_email,
                    "this_year_grade": this_year_grade,
                    "last_year_grade": last_year_grade,
                    "average_grade": average_grade,
                }
                students_data_list.append(personal_data)
            elif another == 'no':
                print("Done with Student Management System ! ")
                logging.info("Student Management System ! ")
                break
            else:
                print("Please enter yes or no.")
                logging.warning("Please enter yes or no.")
        break
    ################################################################# check file's path correctness
    elif file_prompt == 'no':
        path_input = input("Enter the path of the file: ")
        logging.debug(f"Path input from user: [{path_input}]")
        file_path = get_correct_file_path(path_input)
        ################################################################# import students data from file
        students_data_list = get_students_from_file(file_path)
        break
    else:
        print("Please enter yes or no.")
        logging.warning("Please enter yes or no.")


###################################################################################################################################
print("\n________________________________________FINAL RESULTS________________________________________\n")
if students_data_list is None or len(students_data_list) == 0:
    print("No students data was provided, closing Student Management System.")
else:
    ##################################### write students data in the StudentsReport.txt
    write_to_file(students_data_list)
    for i, data in enumerate(students_data_list):
        print(f"{i +1}) Name: {data['name']}, Age: {data['age']}, Email: {data['email']}"
              f"\n Grades: This Year: {data['this_year_grade']}, "
                         f"Last Year: {data['last_year_grade']}, "
                         f"Avg. Grade: {data['average_grade']} \n ")
        logging.info(f"{i +1}) Name: {data['name']}, Age: {data['age']}, Email: {data['email']}"
              f"Grades: This Year: {data['this_year_grade']}, "
                         f"Last Year: {data['last_year_grade']}, "
                         f"Avg. Grade: {data['average_grade']} ")


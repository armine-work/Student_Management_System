import os

from app.students_data import *
from app.validation import get_number, get_full_name
from app.grade_calculation import *
from app.data_files_usage import *

students_data_list = []

############################################### ask import students data manually of from file
while True:
    file_prompt = input("Do you want to provide students list manually? (yes/no): ").lower().strip()
    if file_prompt == 'yes':
    ############################################ ask to input student's name, username
        students_amount = get_number(user_input="How many students do you have? ",
                                            error_msg="Please enter a numeric value.")
        student_count = 0
        while student_count < students_amount:
            another = input("Add a new student? (yes/no): ").lower().strip()
            if another == 'yes':
                student_count += 1
                ########################################################### call student full name
                student_full_name = get_full_name(name=input("What is student's name? ").strip().title(),
                                             surname=input("What is student's surname? ").strip().title())
                #print("full name:", student_full_name)
                ########################################################### call student age
                student_age = get_student_age(student_full_name)
                ########################################################## call students email
                student_email = get_email(student_full_name)
                #print("email:", student_email)
                ########################################################## call students grades
                this_year_grade = get_this_year_grade()
                last_year_grade = get_last_year_grade()
                averageGrade = get_averageGrade(student_full_name, this_year_grade, last_year_grade)
                ######################################################### store student data in a dictionary
                personal_data = {
                    "name": student_full_name,
                    "age": student_age,
                    "email": student_email,
                    "this_year_grade": this_year_grade,
                    "last_year_grade": last_year_grade,
                    "averageGrade": averageGrade,
                }
                students_data_list.append(personal_data)
            elif another == 'no':
                print("Done with Student Management System ! ")
                break
            else:
                print("Please enter yes or no.")
        break
    ################################################################# check file's path correctness
    elif file_prompt == 'no':
        path_input = input("Enter the path of the file: ")
        file_name = "StudentsList.txt"
        if os.path.basename(path_input) == file_name:
            file_path = path_input
        else:
            file_path = os.path.join(path_input, file_name)
        ################################################################# import students data from file
        students_data_list = get_students_from_file(file_path)
        break
    else:
        print("Please enter yes or no.")


###################################################################################################################################
print("\n________________________________________FINAL RESULTS________________________________________\n")
if len(students_data_list) == 0:
    print("No students data was provided, closing Student Management System.")
else:
    ##################################### write students data in the StudentsReport.txt
    write_to_file(students_data_list)
    for i, data in enumerate(students_data_list):
        print(f"{i +1}) Name: {data['name']}, Age: {data['age']}, Email: {data['email']}"
              f"\n Grades: This Year: {data['this_year_grade']}, "
                         f"Last Year: {data['last_year_grade']}, "
                         f"Avg. Grade: {data['averageGrade']} \n ")


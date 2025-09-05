import os
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename= "Logs_Class.txt",
                    format='%(levelname)s - %(name)s - "%(message)s" - %(asctime)s',
                    datefmt='%m/%d/%Y %H:%M:%S %p',
                    filemode='w')

from app.validation import get_number
from app.data_files_usage import get_students_from_file, write_to_file, get_correct_file_path


class StudentClass:
    def __init__(self, name, surname, student_age , this_year_grade, last_year_grade):
        self.name = name
        self.surname = surname
        self.age = student_age
        self.this_year_grade = this_year_grade
        self.last_year_grade = last_year_grade
        self.students_data_list = []

    def get_full_name(self, name, surname):
        self.student_full_name = name + " " + surname
        student_full_name_split = self.student_full_name.split()
        self.student_full_name = " ".join(student_full_name_split)
        #print("full name:", self.student_full_name)
        return self.student_full_name

    existing_emails = []
    ############################################################### get student email
    def get_email(self, student_full_name):
        global existing_emails
        username = student_full_name.replace(" ", ".")
        email_base = username.lower()
        email_domain = "@myschool.armstqb"
        self.email = email_base + email_domain
        ########################################################### check student email uniqueness
        suffix = 1
        while self.email in self.existing_emails:
            self.email = email_base + str(suffix) + email_domain
            suffix += 1
        self.existing_emails.append(self.email)
        return self.email


    def get_student_age(self, student_full_name): ########################3 where to use self?
        while True:
            self.age = get_number(user_input="What is student's age? ", error_msg= "Please, enter valid age between 1-120.")
                ############################################################# checking for valid age range
            if self.age <= 0 or self.age >= 120:
                print("Please, enter valid age between 1-120.")
            elif 0 < self.age < 6:
                print(f"This kid: {student_full_name} is still a Kindergarten student, he/she is not counted.")
            elif self.age < 18:
                print(f"This student: {student_full_name} is a Primary School student, he/she is not counted.")
            else:
                print(f"This student: {student_full_name} is a College student, let's continue.")
                return self.age

################################################################# define This Year Average method
    def get_this_year_grade(self):
        # converting user's input to numeric value for This Year Average Grade data
        while True:
            self.this_year_grade = get_number(user_input="Enter student's average grade for This Year in [0 - 100] range: ",
                                              error_msg="Error, enter numeric, positive value for This Year Grade.")
            if self.this_year_grade < 0 or self.this_year_grade > 100:
                print("Error, This Year Grade should be [0-100].")
            else:
                return self.this_year_grade

############################################################ define Last Year Average methods
    def get_last_year_grade(self):
        # converting user's input to numeric value for Last Year Average Grade data
        while True:
            self.last_year_grade = get_number(user_input="Enter student's average grade for Last Year in [0 - 100] range: ",
                                              error_msg="Error, enter numeric, positive value for Last Year Grade.")
            if self.last_year_grade < 0 or self.last_year_grade > 100:
                print("Error, Last Year Grade should be [0-100].")
            else:
                return self.last_year_grade

##############################################################    calculate averageGrade method
    def get_avarage_grade(self, student_full_name, this_year_grade, last_year_grade):
        self.average_grade = (this_year_grade + last_year_grade) / 2
        # print("The average grade of 2 years is:", averageGrade)
        if 0 <= self.average_grade < 50:
            print(f"The student, {student_full_name}, fails for the next year, because the average grade- [{self.average_grade}] is less than 50.")
        elif self.average_grade == 50:
            print(f"The student, {student_full_name}, passes to the next year with the minimum passing grade- [{self.average_grade}] equals to 50.")
        else:
            print(f"The student, {student_full_name}, passes to the next year, as the average grade- [{self.average_grade}] is more that 50.")

        return self.average_grade


def main():
############################# create a student instant ###########################################
    student = StudentClass(None, None, 0, 0, 0)

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
                    student_full_name = student.get_full_name(name=input("What is student's name? ").strip().title(),
                                                      surname=input("What is student's surname? ").strip().title())
                    logging.debug(f"Inputted Student's full name from user: [{student_full_name}]")
                    ########################################################### call student age
                    student_age = student.get_student_age(student_full_name)
                    logging.debug(f"Inputted student's age from user: [{student_age}]")
                    ########################################################## call students email
                    student_email = student.get_email(student_full_name)
                    logging.debug(f"Student email: [{student_email}]")
                    ########################################################## call students grades
                    this_year_grade = student.get_this_year_grade()
                    logging.debug(f"Student's This year grade: [{this_year_grade}]")
                    last_year_grade = student.get_last_year_grade()
                    logging.debug(f"Student's Last year grade: [{last_year_grade}]")
                    average_grade = student.get_avarage_grade(student_full_name, this_year_grade, last_year_grade)
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
                    student.students_data_list.append(personal_data)
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
            student.students_data_list = get_students_from_file(file_path)
            break
        else:
            print("Please enter yes or no.")
            logging.warning("Please enter yes or no.")

    ###################################################################################################################################
    print("\n________________________________________FINAL RESULTS________________________________________\n")
    if student.students_data_list is None or len(student.students_data_list) == 0:
        print("No students data was provided, closing Student Management System.")
    else:
        ##################################### write students data in the StudentsReport.txt
        write_to_file(student.students_data_list)
        for i, data in enumerate(student.students_data_list):
            print(f"{i + 1}) Name: {data['name']}, Age: {data['age']}, Email: {data['email']}"
                  f"\n Grades: This Year: {data['this_year_grade']}, "
                  f"Last Year: {data['last_year_grade']}, "
                  f"Avg. Grade: {data['average_grade']} \n ")
            logging.info(f"{i + 1}) Name: {data['name']}, Age: {data['age']}, Email: {data['email']}"
                         f"Grades: This Year: {data['this_year_grade']}, "
                         f"Last Year: {data['last_year_grade']}, "
                         f"Avg. Grade: {data['average_grade']} ")



if __name__ == "__main__":
    main()
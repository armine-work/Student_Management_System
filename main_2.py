# Create a script that gets the full name, age, and average grade of a student for the current year and average grade for the previous year.
# If the age of the student is less than 18, print the student’s name, age, and tell that he/she is a Primary School student;
#   otherwise, print that the student is a college student
# Print the average grade of the student for two years.
#  If it is less than 50, tell that the student fails;# otherwise, tell that the student passes.
# Change the code to accept data for more than one student
# Add one more input, which asks about inputting a new student or stopping.
# If yes, continue inputting; if no, stop inputting and print all students’ data.
# Add one more input that asks about the maximum number of students.
# And automatically stop inputting students’ data when it reaches that number
# Change the code to use list(s) for saving the inserted students data
# Use the lists to print the necessary data
# Refactor my code to use at least two types of data structures for working with data:
# For example: Personal data of students as a dictionary, Grades as a tuples
# With string operation, make better formatting for students’ names, like removing extra spaces, and make capitalized name parts
# Create school email addresses for students in this format: name.surname@myschool.armstqb and store them in a data structure associated with students.
# Make sure the uniqueness of the email addresses

students_data_list = []
grades_all_list = []
################################################## get user full name
def get_username(name_input):
    space_count = name_input.count(" ")
    if space_count !=0:
        name_input = name_input.replace(" ", "")
    if name_input.islower() == True:
        name_input = name_input.capitalize()
    if name_input.isupper() == True:
        name_input = name_input.lower().capitalize()

    return name_input

################################################### get user age
def get_student_age(student_full_name):
    while True:
        age_input = input("What is student's age? ")
        if age_input.replace('.', '', 1).isnumeric():
            age = float(age_input)if '.' in age_input else int(age_input)
            # checking for valid age range
            if age <= 0 or age >= 120:
                print("Please, enter valid age between 1-120.")
            elif 0 < age < 6:
                print("This kid: {st} is still a kindergarten student, he/she is not counted.".format(st=student_full_name))
            elif age < 18:
                print("This student: {st} is a Primary School student, he/she is not counted.".format(st=student_full_name))
            else:
                print("This student: {st} is a College student, let's continue. ".format(st=student_full_name))
                return age
        else:
            print("Please, enter valid age between 1-120.")

################################################################################## get users average grade for This year
def get_this_year_grade():
    # converting user's input to numeric value for This Year Average Grade data
    while True:
        thisYearAverage_input = input("Enter student's average grade for this year in [0 - 100] range: ")
        if thisYearAverage_input.replace('.', '', 1).isnumeric():
            thisYearAverage = float(thisYearAverage_input) if '.' in thisYearAverage_input else int(thisYearAverage_input)
            if thisYearAverage < 0 or thisYearAverage > 100:
                print("Error, This Year Grade should be [0-100].")
            else:
                return thisYearAverage
        else:
            print("Error, enter numeric, positive value for This Year Grade.")

################################################################################### get users average grade for LAST year
def get_last_year_grade():
    #converting user's input to numeric value for Last Year Average Grade data
    while True:
        lastYearAverage_input = input("Enter student's average grade for last year in [0 - 100] range: ")
        if lastYearAverage_input.replace('.', '', 1).isnumeric():
            lastYearAverage = float(lastYearAverage_input) if '.' in lastYearAverage_input else int(lastYearAverage_input)
            if lastYearAverage < 0 or lastYearAverage > 100:
                print("Error, Last Year Grade should be [0-100].")
            else:
                return lastYearAverage
        else:
            print("Error, enter numeric, positive value for Last Year Grade.")

#################################################################################### get users average grade for 2 years
def get_averageGrade():
    averageGrade = (this_year_grade + last_year_grade) / 2
    #print("The average grade of 2 years is:", averageGrade)
    if 0 <= averageGrade < 50:
        print(
            f"The student, {student_full_name}, fails for the next year, because the average grade [{averageGrade}] is less than 50.")
    elif averageGrade == 50:
        print(
            f"The student, {student_full_name}, passes to the next year with the minimum passing grade- [{averageGrade}] equals to 50.")
    else:
        print(f"The student, {student_full_name}, passes to the next year, as the average grade [{averageGrade}] is more that 50.")
    return averageGrade

##########################################################################################################################################
students_amount_input  = input("How many students do you have? ").lower()
if students_amount_input.isdigit():
    students_amount = int(students_amount_input)
    student_count = 0

    while student_count < students_amount:
        another = input("Do you want to add a student? (yes/no): ").lower().strip()
        if another == 'yes':
            student_count += 1
            ########################################################### get student full name
            student_name = get_username(name_input=input("What is student's name? "))
            student_surname = get_username(name_input=input("What is student's surname? "))
            student_full_name = student_name + " " + student_surname
            ########################################################### call student age
            student_age = get_student_age(student_full_name)
            ########################################################### get student email
            email_base = student_name.lower() + "." + student_surname.lower()
            email_domain = "@myschool.armstqb"
            email = email_base + email_domain
            ########################################################### check student email uniqueness
            existing_email = []
            for student in students_data_list:
                existing_email.append(student["email"])
            suffix = 1
            while email in existing_email:
                email = email_base + str(suffix) + email_domain
                suffix += 1
            student_email = email
            ######################################################### store student data in a dictionary
            personal_data = {
                "name": student_full_name,
                "age": student_age,
                "email": student_email
            }
            students_data_list.append(personal_data)
            ######################################################### call students grades data and store in a tuple
            this_year_grade = get_this_year_grade()
            last_year_grade = get_last_year_grade()
            averageGrade = get_averageGrade()
            ######################################################## store grades data in a tuple
            grades_tuple = tuple((this_year_grade, last_year_grade, averageGrade))
            ######################################################## store grades data in a list so can be added more data
            grades_all_list.append(grades_tuple)

        elif another == 'no':
            print("Done with Student Management System ! ")
            break
        else:
            print("Please enter yes or no.")
else:
    print("Please, enter valid number for student's amount.")

########################################################################################################################
print("\n________________________________________FINAL RESULTS________________________________________\n")
for i in range(len(grades_all_list)):
    print(f"{i +1}) Name: {students_data_list[i]['name']}, Age: {students_data_list[i]['age']}, Email: {students_data_list[i]['email']}"
          f"\n Grades: This Year: {grades_all_list[i][0]}, Last Year: {grades_all_list[i][1]}, Avg. Grade: {grades_all_list[i][2]} \n")
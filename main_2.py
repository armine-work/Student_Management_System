# Create a script that gets the full name, age, and average grade of a student for the current year and average grade for the previous year.
# If the age of the student is less than 18, print the student’s name, age, and tell that he/she is a Primary School student;
#   otherwise, print that the student is a college student
# Print the average grade of the student for two years.
#  If it is less than 50, tell that the student fails;# otherwise, tell that the student passes.
# Change the code to accept data for more than one student
# Add one more input, which asks about inputting a new student or stopping.
# If yes, continue inputting; if # no, stop inputting and ???print all students’ data.???
# Add one more input that asks about the maximum number of students.
# And automatically stop inputting students’ data when it reaches that number
# Change the code to use list(s) for saving the inserted students data
# Use the lists to print the necessary data
# Refactor my code to use at least two types of data structures for working with data:
# For example: Personal data of students as a dictionary, Grades as a tuples

students_data_list = []
grades_all_list = []
################################################## get user full name
def get_student_name():
    name = input("What is student's name? ")
    surname = input("What is student's surname? ")
    return name + " " + surname

################################################### get user age
def get_student_age(full_name):
    while True:
        age_input = input("What is student's age? ")
        if age_input.replace('.', '', 1).isnumeric():
            age = float(age_input)if '.' in age_input else int(age_input)
            # checking for valid age range
            if age <= 0 or age >= 120:
                print("Please, enter valid age between 1-120.")
            elif 0 < age < 6:
                print("This kid: {st} is still a kindergarten student, he/she is not counted.".format(st=full_name))
            elif age < 18:
                print("This student: {st} is a Primary School student,he/she is not counted.".format(st=full_name))
            else:
                print("This student: {st} is a College student, let's continue: ".format(st=full_name))
                return(age)
        else:
            print("Please, enter valid age between 1-120.")

################################################################################## get users average grade for This year
def get_this_year_grade():
    # converting user's input to numeric value for This Year Average Grade data
    while True:
        thisYearAverage_input = input("Enter student's average grade for this year in [0 - 100] range: ")
        if thisYearAverage_input.replace('.', '', 1).isnumeric():
            thisYearAverage = float(thisYearAverage_input) if '.' in thisYearAverage_input else int(thisYearAverage_input)
            if thisYearAverage <= 0 or thisYearAverage >= 100:
                print("Error, This Year Grade should be [0-100].")
            else:
                return thisYearAverage

################################################################################### get users average grade for LAST year
def get_last_year_grade():
    #converting user's input to numeric value for Last Year Average Grade data
    while True:
        lastYearAverage_input = input("Enter student's average grade for last year in [0 - 100] range: ")
        if lastYearAverage_input.replace('.', '', 1).isnumeric():
            lastYearAverage = float(lastYearAverage_input) if '.' in lastYearAverage_input else int(lastYearAverage_input)
            if lastYearAverage <= 0 or lastYearAverage >= 100:
                print("Error, Last Year Grade should be [0-100].")
            else:
                return lastYearAverage

#################################################################################### get users average grade for 2 years
def get_averageGrade():
    averageGrade = (this_year_grade + last_year_grade) / 2
    #print("The average grade of 2 years is:", averageGrade)
    if 0 <= averageGrade < 50:
        print(
            f"The student, {student_name}, fails for the next year, because the average grade [{averageGrade}] is less than 50.")
    elif averageGrade == 50:
        print(
            f"The student, {student_name}, passes to the next year with the minimum passing grade- [{averageGrade}] equals to 50.")
    else:
        print(f"The student, {student_name}, passes to the next year, as the average grade [{averageGrade}] is more that 50.")
    return averageGrade
##########################################################################################################################################
students_amount_input  = input("How many students do you have? ").lower()
if students_amount_input.isdigit():
    students_amount = int(students_amount_input)
    student_count = 0

    while student_count < students_amount:
        another = input("Do you want to add a student? (yes/no): ").lower()
        if another == 'yes':

            student_name = get_student_name()
            student_age = get_student_age(student_name)
            student_count += 1
            personal_data = {
                "name": student_name,
                "age": student_age,
            }
            students_data_list.append(personal_data)

            this_year_grade = get_this_year_grade()
            last_year_grade = get_last_year_grade()
            averageGrade = get_averageGrade()
            grades_tuple = tuple((this_year_grade, last_year_grade, averageGrade))
            grades_all_list.append(grades_tuple)

        elif another == 'no':
            print("Done with Student Management System ! ")
            break
        else:
            print("Please enter yes or no.")
else:
    print("Please, enter valid number for student's amount.")

########################################################################################################################
print("\n____________________FINAL RESULTS____________________\n")
for i in range(len(grades_all_list)):
    print(f"{i +1}) Name: {students_data_list[i]['name']}, Age: {students_data_list[i]['age']}, "
          f"Grades: This Year: {grades_all_list[i][0]}, Last Year: {grades_all_list[i][1]}, Avg. Grade: {grades_all_list[i][2]}")
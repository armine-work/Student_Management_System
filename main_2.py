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
st_names_list = []
st_age_list = []
st_this_year_grade = []
st_last_year_grade = []
st_avg_grade = []
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
            elif 0 < age <= 6:
                print("This kid: {st} is still a kindergarten student, he/she is not counted.".format(st=full_name))
            elif age <= 18:
                print("This student: {st} is a Primary School student,he/she is not counted.".format(st=full_name))
            else:
                print("This student: {st} is a College student, let's continue: ".format(st=full_name))
                return(age)
        else:
            print("Please, enter valid age between 1-120.")
#################################################### get users average grade for this year
def get_this_year_grade():
    # converting user's input to numeric value for This Year Average Grade data
    while True:
        thisYearAverage_input = input("Enter student's average grade for this year in [0 - 100] range: ")
        if thisYearAverage_input.replace('.', '', 1).isnumeric():
            thisYearAverage = float(thisYearAverage_input) if '.' in thisYearAverage_input else int(thisYearAverage_input)
            return thisYearAverage
#################################################### get users average grade for this year
def get_last_year_grade():
    #converting user's input to numeric value for Last Year Average Grade data
    while True:
        lastYearAverage_input = input("Enter student's average grade for last year in [0 - 100] range: ")
        if lastYearAverage_input.replace('.', '', 1).isnumeric():
            if '.' in lastYearAverage_input:
                lastYearAverage = float(lastYearAverage_input)
            else:
                lastYearAverage = int(lastYearAverage_input)
            return lastYearAverage

#################################################################################################################################
students_amount_input  = input("How many students do you have? ").lower()
if students_amount_input.isdigit():
    students_amount = int(students_amount_input)
    student_count = 0

    while student_count < students_amount:
        another = input("Do you want to add a student? (yes/no): ").lower()
        if another == 'yes':

            student_name = get_student_name()
            st_names_list.append(student_name)

            student_age = get_student_age(student_name)
            st_age_list.append(student_age)

            this_year_grade = get_this_year_grade()
            st_this_year_grade.append(this_year_grade)

            last_year_grade = get_last_year_grade()
            st_last_year_grade.append(last_year_grade)

            if this_year_grade <= 100:
                if last_year_grade <= 100:
                    averageGrade = (this_year_grade + last_year_grade) / 2
                    print("The average grade of 2 years is:", averageGrade)

                    st_avg_grade.append(averageGrade)

                    student_count += 1
                    if 0 <= averageGrade < 50:
                        print(f"The student, {student_name}, fails for the next year, because the average grade [{averageGrade}] is less than 50.")
                    elif averageGrade == 50:
                        print(f"The student, {student_name}, passes to the next year with the minimum passing grade- [{averageGrade}] equals to 50.")
                    else:
                        print(f"The student, {student_name}, passes to the next year, as the average grade [{averageGrade}]")
                else:
                    print("Please, enter valid grade for the Last Year Grade [0-100].")
            else:
                print("Please, enter valid grade for the This Year Grade [-100].")
        elif another == 'no':
            print("Done with Student Management System. ")
            break
        else:
            print("Please enter yes or no.")
else:
    print("Please, enter valid number for student's amount.")

########################################################################################################################
print("____________________FINAL RESULTS____________________")
for i in range(len(st_names_list)):
    print(f" {i+1}) Full name: {st_names_list[i]}, Age: {st_age_list[i]},"
          f" This year avg. grade: {st_this_year_grade[i]}, Lastyear avg. grade: {st_last_year_grade[i]},"
          f" The avg. grade of two years: {st_avg_grade[i]}")
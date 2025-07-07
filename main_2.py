# Create a script that gets the full name, age, and average grade of a student for the current year and
# average grade for the previous year.
# If the age of the student is less than 18, print the student’s name, age, and tell that he/she is a Primary School student;
#   otherwise, print that the student is a college student
# Print the average grade of the student for two years.
#   If it is less than 50, tell that the student fails;# otherwise, tell that the student passes.
# Change the code to accept data for more than one student
# • Add one more input, which asks about inputting a new student or stopping.
# If yes, continue inputting; if # no, stop inputting and ???print all students’ data.???
# • Add one more input that asks about the maximum number of students.
# And automatically stop inputting students’ data when it reaches that number

students_amount_input  = input("How many students do you have? ")
if students_amount_input.isdigit():
    students_amount = int(students_amount_input)
    student_count = 0
    while True:
        if student_count < students_amount:
            another = input("Do you want to add a student? (yes/no): ").lower()
            if another == 'yes':

                name = input("What is student's name? ")
                surname = input("What is student's surname? ")
                full_name = name + " " + surname
                # converting user's input to numeric value for Age
                age_input = input("What is student's age? ")
                if age_input.replace('.', '', 1).isnumeric():
                    if '.' in age_input:
                        age = float(age_input)
                    else:
                        age = int(age_input)
                    # checking for valid age range
                    if age <= 0 or age >= 120:
                        print("Please, enter valid age between 1-120.")
                    elif 0 < age <= 6:
                        print("This kid: {st} is still a kindergarten student, he/she doesn't counted.".format(st=full_name))
                    elif age <= 18:
                        print("This student: {st} is a Primary School student, he/she doesn't counted.".format(st=full_name))
                    else:
                        print("This student: {st} is a College student".format(st=full_name))
                        # converting user's input to numeric value for This Year Average Grade data
                        thisYearAverage_input = input("Enter student's average grade for this year in [0 - 100] range: ")
                        if thisYearAverage_input.replace('.', '', 1).isnumeric():
                            if '.' in thisYearAverage_input:
                                thisYearAverage = float(thisYearAverage_input)
                            else:
                                thisYearAverage = int(thisYearAverage_input)
                            # check for valid grade range
                            if thisYearAverage > 100:
                                print("Please, enter valid grade between 0-100.")
                            else:
                                # converting user's input to numeric value for Last Year Average Grade data
                                lastYearAverage_input = input("Enter student's average grade for last year in [0 - 100] range: ")
                                if lastYearAverage_input.replace('.', '', 1).isnumeric():
                                    if '.' in lastYearAverage_input:
                                        lastYearAverage = float(lastYearAverage_input)
                                    else:
                                        lastYearAverage = int(lastYearAverage_input)
                                    # checking for valid grade range
                                    if lastYearAverage > 100:
                                        print("Please, enter valid grade between 0-100.")
                                    else:
                                        averageGrade = (thisYearAverage + lastYearAverage) / 2
                                        print("The average grade of 2 years is:", averageGrade)
                                        student_count += 1
                                        if 0 <= averageGrade < 50:
                                            print(
                                                f"The student, {full_name}, fails for the next year, because the average grade [{averageGrade}] is less than 50.")
                                        elif averageGrade == 50:
                                            print(f"The student, {full_name}, passes to the next year with the minimum passing grade- [{averageGrade}] equals to 50.")
                                        else:
                                            print(f"The student, {full_name}, passes to the next year, as the average grade [{averageGrade}] is greater than 50.")
                                else:
                                    print("Please, enter numeric, positive value for Last Year Grade.")
                        else:
                            print("Please, enter numeric, positive value for This Year Grade.")
                else:
                    print("Please, enter a numeric, positive value for age.")
            elif another == 'no':
                break
            else:
                print("Please enter yes or no.")
        elif student_count == students_amount:
            print(f"The students data filling process ends, as the student count {student_count} reaches to the student amount {students_amount}.")
            break
else:
    print("Please enter a valid number.")






# Create a script that gets the full name, age, and average grade of a student for the current year and
# average grade for the previous year.
# If the age of the student is less than 18, print the student’s name, age, and tell that he/she is a Primary School student;
#   otherwise, print that the student is a college student
# Print the average grade of the student for two years.
#   If it is less than 50, tell that the student fails;# otherwise, tell that the student passes.
name = input("What is your name? ")
surname = input("What is your surname? ")
full_name = name + " " + surname
try:
    age = int(input("What is your age? "))
    if age <= 0 or age >= 120:
        print("Error: The age cannot be less than or equal 0 and greater than 120.")
    elif 0 < age <= 6:
            print("This kid: {st} is still a kindergarten student".format(st=full_name))
    elif age <= 18:
        print("This student: {st} is a Primary School student ".format(st=full_name))
    else:
        print("This student: {st} is a College student ".format(st=full_name))
        thisYearAverage = float(input("Enter your average grade for this year in [0 - 100] range: "))
        if thisYearAverage < 0 or thisYearAverage > 100:
            print("Error: The average grade of this year cannot be less than 0 or greater than 100.")
        else:
            lastYearAverage = float(input("Enter your average grade for last year in [0 - 100] range: "))
            if lastYearAverage < 0 or lastYearAverage > 100:
                print("Error: The average grade of the previous year cannot be less than 0 or greater than 100.")
            else:
                averageGrade = (thisYearAverage + lastYearAverage) / 2
                print("The average grade of 2 years is:", averageGrade)
                if 0 <= averageGrade < 50:
                    print(f"The student {full_name} fails for the next year, because the average grade is less than: {averageGrade}")
                else:
                    print(f"The student {full_name} passes to the next year, as the average grade is greater than {averageGrade}")
except ValueError:
    print("Please enter a numerical value for age and grades.")
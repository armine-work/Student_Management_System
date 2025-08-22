import os

students_data_list = []
grades_all_list = []
################################################## get user full name
def get_full_name(name, surname):
    student_full_name = name + " " + surname
    student_full_name_split = student_full_name.split()
    student_full_name = " ".join(student_full_name_split)
    #print("full name:", student_full_name)
    return student_full_name

########################################################### get student email
def get_email(student_full_name):
    username = student_full_name.replace(" ", ".")
    email_base = username.lower()
    email_domain = "@myschool.armstqb"
    email = email_base + email_domain
    # print("email:", email)
    ########################################################### check student email uniqueness
    existing_email = []
    for student in students_data_list:
        existing_email.append(student["email"])
    suffix = 1
    while email in existing_email:
        email = email_base + str(suffix) + email_domain
        suffix += 1
    student_email = email
    return student_email

################################################### get user age
def get_student_age(student_full_name):
    while True:
        age_input = input("What is student's age? ")
        if age_input.replace('.', '', 1).isnumeric():
            age = float(age_input)if '.' in age_input else int(age_input)
            ############################################################# checking for valid age range
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
def get_averageGrade(student_full_name, this_year_grade, last_year_grade):
    averageGrade = (this_year_grade + last_year_grade) / 2
    if 0 <= averageGrade < 50:
        print(f"The student, {student_full_name}, fails for the next year, because the average grade [{averageGrade}] is less than 50.")
    elif averageGrade == 50:
        print(f"The student, {student_full_name}, passes to the next year with the minimum passing grade- [{averageGrade}] equals to 50.")
    else:
        print(f"The student, {student_full_name}, passes to the next year, as the average grade [{averageGrade}] is more that 50.")
    return averageGrade

############################################################################# get student's data from file
def get_students_from_file(file_path):
    try:
        with open(file_path, "r") as students_file:
            lines = students_file.readlines()
            for line in lines:
                line = line.strip()
                parts = line.split(',')
                if len(parts) < 4:
                    print("Invalid line in the file, skipping:", line)
                    continue
                else:
                    student_full_name = parts[0].strip()
                    student_age = int(parts[1].strip())
                    this_year_grade = float(parts[2].strip())
                    last_year_grade = float(parts[3].strip())

                    student_email = get_email(student_full_name)
                    averageGrade = get_averageGrade(student_full_name, this_year_grade, last_year_grade)

                    students_data_list.append({"name": student_full_name,
                        "age": student_age,
                        "email": student_email,
                        "this_year_grade": this_year_grade,
                        "last_year_grade": last_year_grade,
                        "averageGrade": averageGrade})
            return students_data_list
        
    except FileNotFoundError as error:
        print("File not found. Please try again.", error)
        return None
    except Exception as error:
        print("An error appeared:", error)
        return None

############################################### ask import students data manually of from file
while True:
    file_prompt = input("Do you want to provide students list manually? (yes/no): ").lower().strip()
    if file_prompt == 'yes':
    ####################################################################################
        students_amount_input = input("How many students do you have? ").lower()
        if students_amount_input.isdigit():
            students_amount = int(students_amount_input)
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
        else:
            print("Please, enter valid number for student's amount.")
            continue
        break
    ################################################################# check file's path correctness
    elif file_prompt == 'no':
        path_input = input("Enter the path of the file: ").strip()
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


################################################################################## write students data in the StudentsReport.txt
with open("StudentsReport.txt", "w") as report:
    for i, data in enumerate(students_data_list):
        report.write(f"{i + 1}) Name: {data['name']}, Age: {data['age']}, Email: {data['email']}"
                     f"\n Grades: This Year: {data['this_year_grade']}, "
                     f"Last Year: {data['last_year_grade']}, "
                     f"Avg. Grade: {data['averageGrade']} \n")
print("Students data is stored in StudentsReport.txt")

###################################################################################### print Students data
print("\n________________________________________FINAL RESULTS________________________________________\n")
if len(students_data_list) == 0:
    print("No students data was provided, closing Student Management System.")
else:
    for i, data in enumerate(students_data_list):
        print(f"{i +1}) Name: {data['name']}, Age: {data['age']}, Email: {data['email']}"
              f"\n Grades: This Year: {data['this_year_grade']}, "
                         f"Last Year: {data['last_year_grade']}, "
                         f"Avg. Grade: {data['averageGrade']} \n")
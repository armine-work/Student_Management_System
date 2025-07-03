name = input("What is your name? ")
surname = input("What is your surname? ")
full_name = name + " " + surname
#converting user's input to numeric value for Age
age_input = input("What is your age? ")
if age_input.replace('.', '', 1).isnumeric():
    if '.' in age_input:
        age = float(age_input)
    else:
        age = int(age_input)
    #checking for valid age range
    if age <= 0 or age >= 120:
        print("Please, enter valid age between 1-120.")
    elif 0 < age <= 6:
            print("This kid: {st} is still a kindergarten student".format(st=full_name))
    elif age <= 18:
        print("This student: {st} is a Primary School student ".format(st=full_name))
    else:
        print("This student: {st} is a College student ".format(st=full_name))
        #converting user's input to numeric value for This Year Average Grade data
        thisYearAverage_input = input("Enter your average grade for this year in [0 - 100] range: ")
        if thisYearAverage_input.replace('.', '', 1).isnumeric():
            if '.' in thisYearAverage_input:
                thisYearAverage = float(thisYearAverage_input)
            else:
                thisYearAverage = int(thisYearAverage_input)
            #check for valid grade range
            if thisYearAverage > 100:
                print("Please, enter valid grade between 0-100.")
            else:
                # converting user's input to numeric value for Last Year Average Grade data
                lastYearAverage_input = input("Enter your average grade for last year in [0 - 100] range: ")
                if lastYearAverage_input.replace('.', '', 1).isnumeric():
                    if '.' in lastYearAverage_input:
                        lastYearAverage = float(lastYearAverage_input)
                    else:
                        lastYearAverage = int(lastYearAverage_input)
                    #checking for valid grade range
                    if lastYearAverage > 100:
                        print("Please, enter valid grade between 0-100.")
                    else:
                        averageGrade = (thisYearAverage + lastYearAverage) / 2
                        print("The average grade of 2 years is:", averageGrade)
                        if 0 <= averageGrade < 50:
                            print(f"The student, {full_name}, fails for the next year, because the average grade [{averageGrade}] is less than 50.")
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

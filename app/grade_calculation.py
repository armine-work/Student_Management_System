import logging
logger = logging.getLogger(__name__)

from app.validation import get_number
################################################################################## get users average grade for This year
def get_this_year_grade():
    # converting user's input to numeric value for This Year Average Grade data
    while True:
        thisYearAverage = get_number(user_input="Enter student's average grade for This Year in [0 - 100] range: ",
                                     error_msg="Error, enter numeric, positive value for This Year Grade.")
        logging.info(f"Enter student's average grade for This Year in [0 - 100] range")
        if thisYearAverage < 0 or thisYearAverage > 100:
            print("Error, This Year Grade should be [0-100].")
        else:
            return thisYearAverage


################################################################################### get users average grade for LAST year
def get_last_year_grade():
    #converting user's input to numeric value for Last Year Average Grade data
    while True:
        lastYearAverage = get_number(user_input="Enter student's average grade for Last Year in [0 - 100] range: ",
                                              error_msg="Error, enter numeric, positive value for Last Year Grade.")
        logger.info(f"Enter student's average grade for Last Year in [0 - 100] range: ")
        if lastYearAverage < 0 or lastYearAverage > 100:
            print("Error, Last Year Grade should be [0-100].")
        else:
            return lastYearAverage


#################################################################################### get users average grade for 2 years
def get_averageGrade(student_full_name, this_year_grade, last_year_grade):
    averageGrade = (this_year_grade + last_year_grade) / 2
    # print("The average grade of 2 years is:", averageGrade)
    if 0 <= averageGrade < 50:
        print(f"The student, {student_full_name}, fails for the next year, because the average grade- [{averageGrade}] is less than 50.")
        logger.info(f"The student, {student_full_name}, fails for the next year, because the average grade- [{averageGrade}] is less than 50.")
    elif averageGrade == 50:
        print(f"The student, {student_full_name}, passes to the next year with the minimum passing grade- [{averageGrade}] equals to 50.")
        logger.info(f"The student, {student_full_name}, passes to the next year with the minimum passing grade- [{averageGrade}] equals to 50.")
    else:
        print(f"The student, {student_full_name}, passes to the next year, as the average grade- [{averageGrade}] is more that 50.")
        logger.info(f"The student, {student_full_name}, passes to the next year, as the average grade- [{averageGrade}] is more that 50.")
    return averageGrade
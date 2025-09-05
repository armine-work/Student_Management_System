import os
import logging
logger = logging.getLogger(__name__)

from app.students_data import get_email
from app.grade_calculation import get_average_grade

students_data_list = []

################################################### get correct file path
def get_correct_file_path(path_input):
    while True:
        file_name = "StudentsList.txt"
        if os.path.exists(path_input):
            logger.debug(f"Correct file path [{path_input}]")
            if os.path.basename(path_input):
                logger.debug(f"path has basename [{path_input}]")
                if os.path.basename(path_input)== file_name:
                    file_path = path_input
                    logger.debug(f"file path is correct: [{file_path}]")
                    return file_path
                else:
                    file_path = os.path.join(path_input, file_name)
                    logger.debug(f"file name is added to folder path: [{file_path}]")
                    return file_path
            else:
                logger.debug(f"path doesn't have base name ;;;;;;;;;;.[{path_input}]")
                return None
        else:
            logger.debug(f"File path incorrect ---- [{path_input}]")
            return None

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
                    logger.warning(f"Invalid line in the file, skipping: [{line}]")
                    continue
                else:
                    student_full_name = parts[0].strip()
                    logger.debug(f"Student's full name from file: [{student_full_name}]")
                    student_age = int(parts[1].strip())
                    logger.debug(f"Student's age from file: [{student_age}]")
                    this_year_grade = float(parts[2].strip())
                    logger.debug(f"Student's this year grade: [{this_year_grade}]")
                    last_year_grade = float(parts[3].strip())
                    logger.debug(f"Student's last year grade: [{last_year_grade}]")
                    ############################################ create student email
                    student_email = get_email(student_full_name)
                    logger.debug(f"Student's email from file: [{student_email}]")
                    ############################################ get average grade of 2 years
                    average_grade = get_average_grade(student_full_name, this_year_grade, last_year_grade)
                    logger.debug(f"Student's average grade: [{average_grade}]")
                    ############################################  store students data in a list of dictionary
                    students_data_list.append({
                        "name": student_full_name,
                        "age": student_age,
                        "email": student_email,
                        "this_year_grade": this_year_grade,
                        "last_year_grade": last_year_grade,
                        "average_grade": average_grade})
            return students_data_list
    except FileNotFoundError as error:
        print("File not found. Please try again.", error)
        logger.error(f"File not found. Please try again.{error}")
        return None

    except Exception as error:
        print("An error appeared:", error)
        logger.error(f"An error appeared:{error}")
        return None


############################################################################### write student data in StudentReport.txt
def write_to_file(students_data_list):
    with open("StudentsReport.txt", "a") as report:
        for i, data in enumerate(students_data_list):
            report.write(f"{i + 1}) Name: {data['name']}, Age: {data['age']}, Email: {data['email']}"
                         f"\n Grades: This Year: {data['this_year_grade']}, "
                         f"Last Year: {data['last_year_grade']}, "
                         f"Avg. Grade: {data['average_grade']} \n ")
    logger.info("Students data is stored in StudentsReport.txt")




import os
import logging
logger = logging.getLogger(__name__)

################################################### validated inputed number
def get_number(user_input, error_msg):
    while True:
        number = input(user_input).strip()
        logger.debug(f"Inputted number from user: [{number}]")
        if number.replace(" ", "", 1).isdigit():
            number = float(number) if '.' in number else int(number)
            return number
        else:
            print(error_msg)
            logger.debug(error_msg)


################################################## get user full name
def get_full_name(name, surname):
    student_full_name = name + " " + surname
    student_full_name_split = student_full_name.split()
    student_full_name = " ".join(student_full_name_split)
    #print("full name:", student_full_name)
    return student_full_name


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


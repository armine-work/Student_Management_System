
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
    print("full name:", student_full_name)
    return student_full_name




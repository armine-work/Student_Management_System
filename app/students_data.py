import logging
logger = logging.getLogger(__name__)

from app.validation import get_number, get_full_name

existing_emails = []
############################################################### get student email
def get_email(student_full_name):
    #global existing_emails
    username = student_full_name.replace(" ", ".")
    email_base = username.lower()
    email_domain = "@myschool.armstqb"
    email = email_base + email_domain
    ########################################################### check student email uniqueness
    suffix = 1
    while email in existing_emails:
        email = email_base + str(suffix) + email_domain
        suffix += 1
    existing_emails.append(email)
    return email


################################################### get user age
def get_student_age(student_full_name):
    while True:
        age = get_number(user_input="What is student's age? ", error_msg= "Please, enter valid age between 1-120.")
            ############################################################# checking for valid age range
        if age <= 0 or age >= 120:
            print("Please, enter valid age between 1-120.")
            logger.warning("Please, enter valid age between 1-120.")

        elif 0 < age < 6:
            print("This kid: {st} is still a kindergarten student, he/she is not counted.".format(st=student_full_name))
            logger.info(f"This kid: {student_full_name} is still a kindergarten student, he/she is not counted.")
        elif age < 18:
            print("This student: {st} is a Primary School student, he/she is not counted.".format(st=student_full_name))
            logger.info(f"This student: {student_full_name} is a Primary School student, he/she is not counted.")
        else:
            print("This student: {st} is a College student, let's continue. ".format(st=student_full_name))
            logger.info(f"This student: {student_full_name} is a College student, let's continue.")
            return age


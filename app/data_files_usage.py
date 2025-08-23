from app.students_data import get_email
from app.grade_calculation import get_averageGrade

############################################################################# get student's data from file
def get_students_from_file(file_path):
    students_data_list = []
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
                    ############################################ create student email
                    student_email = get_email(student_full_name)
                    ############################################ get average grade of 2 years
                    averageGrade = get_averageGrade(student_full_name, this_year_grade, last_year_grade)
                    ############################################  store students data in a list of dictionary
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
        print("an error appeared:", error)
        return None


############################################################################### write student data in StudentReport.txt
def write_to_file(students_data_list):
    with open("StudentsReport.txt", "a") as report:
        for i, data in enumerate(students_data_list):
            report.write(f"{i + 1}) Name: {data['name']}, Age: {data['age']}, Email: {data['email']}"
                         f"\n Grades: This Year: {data['this_year_grade']}, "
                         f"Last Year: {data['last_year_grade']}, "
                         f"Avg. Grade: {data['averageGrade']} \n ")
    #print("Students data is stored in StudentsReport.txt")


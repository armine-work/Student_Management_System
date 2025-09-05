# Student Management System

main.py  
• Initialize a Python project in PyCharm called Student Management System.  
• Create a script called main.py.    
• Create a script that gets the full name, age, and average grade of a student for the current year and average grade for the previous year.  
• If the age of the student is less than 18, print the student’s name, age, and tell that he/she is a Primary School student; otherwise, print that the student is a college student.  
• Print the average grade of the student for two years. If it is less than 50, tell that the student fails; otherwise, tell that the student passes.  

main-2.py (module)  
• Change the code to accept data for more than one student.  
• Add one more input, which asks about inputting a new student or stopping.  
•  If yes, continue inputting; if no, stop inputting and print all students’ data.  
• Add one more input that asks about the maximum number of students.  
• And automatically stop inputting students’ data when it reaches that number.  

feature_lists (branch)  
• Change the code to use list(s) for saving the inserted students data.  
• Use the lists to print the necessary data.  

feature-refactor (branch)  
• Refactor code to use at least two types of data structures for working with data:  
• For example: Personal data of students as a dictionary, Grades as a tuples.  

feature-add-email (branch)  
• With string operation, make better formatting for students’ names, like removing extra spaces, and make capitalized name parts.  
• Create school email addresses for students in this format: name.surname@myschool.armstqb and store them in a data structure associated with students.  
• Make sure the uniqueness of the email addresses.  

feature_data_from_files (branch)  
• In the current main.py, add a new input value that will check if students’ data will be provided manually or from a file.  
• If Yes, the program should work as before (in terms of input).  
• If No, the program should read data from a file called “StudentsList.txt”. File path must be an additional input.  
•    Input file one line: Name, Surname, age, pyg, cyg.  
• Write the students’ data to a file called “StudentsReport.txt”.  

feature_modules (branch)  
• Create functions for the code (repeated codes and logical units must be in functions)  
• Create module(s) and/or packages for those functions  

feature_logging (branch)  
• Add logs for all print functions, and store them in separate file.  

feature_class (branch)  
• Create a Student class with its constructor, attributes, and methods.  
• All input data related to student needs must be kept in the class object(s)  
• All output data should be stored or taken from the student objects   
• Hints:  
• • You can create a list of objects of the Student class and manipulate it  
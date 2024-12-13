# Setup inputs
options_input = ""
student_input_a = ""
student_input_b = ""
student_input_c = ""
student_input_d = ""
student_input_e = ""
student_input_f = ""
student_input_g = ""
student_input_h = ""
student_input_i = ""
student_input_j = ""
student_input_k = ""
math_grade = ""
science_grade = ""
ethics_grade = ""
subject_math_input = ""
subject_science_input = ""
subject_ethics_input = ""

# student_input_b = str(student_input_b)
# student_input_a = str(student_input_a)
# options_input = str(options_input)

# Setup lists
student_group_list = []
student_name_list = []
student_id_list = []
student_age_list = []
student_id = 1 # Student id starts with 1
student_group_zip_list = []
student_score_list = []
subject_list = []
subject_math_list = []
subject_science_list = []
subject_ethics_list = []
student_group_score_list = []
# Created a pre-made subject list
subject_list = ["Math", "Science", "Ethics"]

# Setup subject variables
subject_a = ""

#----------------------------------------------------------
# Create a while loop so that the user can be redirected to menu options
# while options_input != ["1", "2", "3"] or student_input_a == "No" or student_input_b == "No" or student_input_c == "Yes" or student_input_d == "Yes":
# print("Hello, how are you?")
# print("What can we do for you?")
# print("You can enter the following")
# Created a list for the options that the user will have to choose
# list_options = ["1. See Students", "2. See Subjects,", "3. See Students, Subjects, and Grades"]
# options_input = input(list_options)
# Used an input function for the list_options
# break
# Add break statement to break the loop
#while options_input != ["1", "2", "3"]:
#----------------------------------------------------------

# Created a main_menu function to call it whenever needed
def main_menu():
    print("Hello, how are you?")
    print("What can we do for you?")
    print("You can enter the following")
    options_input = input("1. See Students, " "2. See Subjects, " "3. See Students, Subjects, and Grades")
    return options_input

# Created an assign_grad function so that I can call it to grade the score provided
def assign_grade(score):
    if 100 <= score >= 85:
        grade = "High Distinction"
    elif 84 <= score >= 70:
        grade = "Distinction"
    elif 69 <= score >= 50:
        grade = "Credit"
    elif 49 <= score >= 35:
        grade = "Pass"
    elif score <= 34:
        grade = "Fail"
    print(grade)


while True:
    options_input = main_menu()

    # Option 1: See Students
    if options_input == "1":
        if len(student_group_list) == 0: # If the student_group_list is empty
            print("No students found.")
            print("Want to add a student?")
            student_input_a = input("Yes or No")
            if student_input_a == "Yes":
                while True:

            # ----------------------------------------------------------
            #while student_input_b == "Yes":
                #student_input_b = student_input_a == "Yes"
            # ----------------------------------------------------------

                    student_name = input("Please enter student's name: ")
                    student_age = input("Please enter student's age: ")


                    # Append details to respective lists
                    student_name_list.append(student_name)
                    student_id_list.append(student_id)
                    student_age_list.append(student_age)

                    # ----------------------------------------------------------
                    # student_group_zip_list = list(zip(student_id_list, student_name_list, student_age_list))
                    # student_group_list.append(student_group_zip_list.pop())
                    # ----------------------------------------------------------

                    # Zip lists into 1 variable
                    student_group_zip_list = list(zip(student_id_list, student_name_list, student_age_list))
                    student_group_list.append(student_group_zip_list[-1])
                    # Append zip list to the group list

            #----------------------------------------------------------
            # Setup variable and list for the Student ID
            # Create a list for the student ID
            # student_id = len(student_name_list)
            # Append inputted age in the student age list
            # Zip all list to form a group
            # student_group_zip_list = list(zip(student_id_list, student_name_list, student_age_list))
            # ----------------------------------------------------------

                    print("You have added:")
                    print(f"ID: {student_id_list.pop()}, Name: {student_name_list.pop()}, Age: {student_age_list.pop()}")

                    student_id += 1 # since we need the student id to increase incrementally

                    print("Do you want to add another student?")
                    student_input_b = input("1. Yes  2. No")
                    if student_input_b == "No":
                        break # to break the loop

                    # ----------------------------------------------------------
                    # student_input_b = student_input_a == "Yes"
                    # elif student_input_b == "No":
                    # print("Do you want to go back to main menu?")
                    # student_input_d = input("1. Yes 2. No")
                    # if student_input_d == "Yes":
                    # main_menu()
                    # elif student_input_d == "No":
                    # print("Thank you!")
                    # break
                    # ----------------------------------------------------------

            if student_input_a == "No":
                print("Want to go back to main menu?")
                student_input_c = input("1. Yes  2. No")
                if student_input_c == "Yes":
                    main_menu()
            else:
                print("Please enter a valid option")
                print("Only enter by 'Yes' or 'No'")
        else:
            print("Student List: ")
            print(student_group_list)
            for sid, name, age in student_group_list:
                print(f"ID: {student[0][0]}, Name: {student[0][1]}, Age: {student[0][2]}")

# Option 2: See Subjects
    elif options_input == "2":
       # if len(student_score_list) == 0:
        print(subject_list)
        print("Would you like to go back to main menu?")
        subject_input_a = input("Yes or No?")
        if  subject_input_a == "Yes":
            main_menu()
        elif subject_input_a == "No":
            main_menu() # call main menu function

# Option 3: See Grades
    elif options_input == "3":
        if len(student_group_list) == 0: # no existing student
            print("No students found")
            print("Would you like to add students?")
            student_input_h = input("Yes or No")
            if student_input_h == "Yes":
                student_input_h = student_input_a
        elif len(student_group_score_list) == 0:
                    print("Students have no grades yet")
                    print("Would you like to add scores?")
                    student_input_i = input("Yes or No")
                    if student_input_i == "Yes":
                        print("Which student do you want to add scores?")
                        student_input_j = int(input("Please enter student id"))
                        if student_input_j in student_id_list:
                            student_input_k = student_id_list.index(student_input_j)
                            student_input_k = int(student_input_k)

                        # print(student_group_list[student_input_k])
                        # print(subject_list[0])

                        print(f"Student Details: [student_group_list[student_input_k]]")
                        print(f"Subjects: {subject_list}") # Print list of subjects

                        # For Debugging
                        # print(f"Student Input J: {student_input_j}, Type: {type(student_input_j)}")
                        # print(f"Student Input K: {student_input_k}, Type: {type(student_input_k)}")

                        # Allow user to input scores for each subject
                        subject_math_input = input("Please enter score for Math")
                        subject_science_input = input("Please enter score for Science")
                        subject_ethics_input = input("Please enter score for Ethics")

                        # Append scores to list of each subjects
                        subject_math_list.append(subject_math_input)
                        subject_science_list.append(subject_science_input)
                        subject_ethics_list.append(subject_ethics_input)

                        # Zip lists of all subjects
                        subject_list_zip = list(zip(subject_math_list, subject_science_list, subject_ethics_list))
                        # Append score to the inputted student
                        student_group_score_list.append(subject_list_zip[student_input_k])

                        print("Scores added successfully")

        elif len(student_score_list) != 0:
            print("Student List: ")
            student_score_zip = list(zip(student_group_zip_list, subject_list))
            print(student_score_zip)
            print("Do you want to add grades to each student?")
            student_input_e = input("Yes or No")
            if student_input_e == "Yes":
                student_input_f = input("Please enter student ID number")
                student_input_g = student_input_f - 1
                print(student_group_zip_list + [student_input_g])
                print("Please enter now the score of " + student_input_g)

            # Enter scores of each subject
                subject_math_input = int(input("Enter score for Math: "))
                subject_science_input = int(input("Enter score for Science: "))
                subject_ethics_input = int(input("Enter score for Ethics: "))

                # Assign grades using assign_grade
                math_grade = assign_grade(subject_math_input)
                science_grade = assign_grade(subject_science_input)
                ethics_grade = assign_grade(subject_ethics_input)

            # Append scores entered
                subject_math_list.append(subject_math_input)
                subject_science_list.append(subject_science_input)
                subject_ethics_list.append(subject_ethics_input)

                student_scores = {"Math": subject_math_input, "Science": subject_science_input, "Ethics": subject_ethics_input,}

                student_group_score_list.append(student_scores)

            # Print student details with scores
                print(student_group_zip_list)

            elif student_input_e == "No":
                print("Student List: ")
                student_score_zip = list(zip(student_group_zip_list, subject_list))
                print(student_group_zip_list)

    else:
        print("Please enter a valid option") # error state

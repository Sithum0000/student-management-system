students = {}

while True:
    print('''
1. Add Student
2. View All Students
3. Search Student by ID
4. Calculate Average Marks
5. Display Highest Scoring Student
6. Exit
''')

    inp = int(input("Enter your choice (1-6): "))

    if inp == 1:
        st_id = input("student id : ")
        name = input("student name : ")
        # Convert marks to integers so you can do math later
        marks = int(input("programming marks : "))
        data_m = int(input("data base marks : "))
        net_m = int(input("networking marks : "))

        # Use the ID as the key, and store a nested dictionary as the value
        students[st_id] = {
            "student name": name,
            "programming marks": marks,
            "data base marks": data_m,
            "networking marks": net_m
        }
        print(f"Student {name} added successfully!")
        
    elif inp == 2:
        print(students)


    elif inp == 3:
        input_id = input("Enter student ID to search: ")
        if input_id in students:
            print(f"Student found: {students[input_id]}")
        else:
            print("Student not found.")

    elif inp == 4:
        student_id=input("Enter student ID to calculate average marks: ")
        if student_id in students:
            marks=students[student_id]["programming marks"]
            data_m=students[student_id]["data base marks"]
            net_m=students[student_id]["networking marks"]
            avg=(marks+data_m+net_m)/3
            print(f"Average marks for {students[student_id]['student name']}: {avg}")
            students[student_id]["average marks"] = avg

    elif inp == 5:
        if students:
            # Calculate the average on the fly to prevent KeyError
            highest_student = max(
                students, 
                key=lambda k: (students[k]["programming marks"] + 
                               students[k]["data base marks"] + 
                               students[k]["networking marks"]) / 3
            )
            
            # Calculate the highest average to display it
            highest_avg = (students[highest_student]["programming marks"] + 
                           students[highest_student]["data base marks"] + 
                           students[highest_student]["networking marks"]) / 3
            
            print(f"Highest scoring student: {students[highest_student]['student name']} with average marks: {highest_avg:.2f}")
        else:
            print("No students available.")

    elif inp == 6:
        print("Program ended")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

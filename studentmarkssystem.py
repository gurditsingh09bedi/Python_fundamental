def store_student_details(num_students, num_subjects):
    student_details = {}
    for i in range(num_students):
        name = input("Enter student name: ")

        subject_marks = {}
        for j in range(num_subjects):
            subject = input("Enter subject name for {}: ".format(name))
            mark = float(input("Enter marks for {} in {}: ".format(name, subject)))
            subject_marks[subject] = mark

        student_details[name] = subject_marks
    return student_details

def display_subject_marks_for_student(student_details, target_name):
    if target_name in student_details:
        print("\nSubject marks for {}:".format(target_name))
        subjects = student_details[target_name]
        for subject, mark in subjects.items():
            print("Subject: {}, Marks: {}".format(subject, mark))
    else:
        print("Student not found.")

def main():
    num_students = int(input("Enter the number of students: "))
    num_subjects = int(input("Enter the number of subjects: "))

    student_details = store_student_details(num_students, num_subjects)

    target_name = input("Enter the student name to display subject marks: ")

    display_subject_marks_for_student(student_details, target_name)

if __name__ == "__main__":
    main()

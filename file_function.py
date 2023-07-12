def write_student_info(roll_number, name, class_name, file="student_info.txt"):
    try:
        file_obj = open(file, "a")
        student_data = f"{roll_number}, {name}, {class_name}\n"
        file_obj.writelines(student_data)
        file_obj.close()
    except IOError as e:
        print(f"An error occurred while opening or writing to the file: {e}")

def print_student_info(file="student_info.txt"):
    try:
        file_obj = open(file, "r")
        data = file_obj.readlines()
        file_obj.close()
        print("Student Information:")
        for line in data:
            print(line.strip())
    except IOError as e:
        print(f"An error occurred while opening or reading the file: {e}")

# Example usage:
write_student_info(1, "John Doe", "Class A")
write_student_info(2, "Jane Smith", "Class B")
print_student_info()

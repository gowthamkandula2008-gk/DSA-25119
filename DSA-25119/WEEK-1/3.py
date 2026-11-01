def find_employee(employees, target_id, position):
    if position >= len(employees):
        return False

    if employees[position] == target_id:
        return True

    return find_employee(employees, target_id, position + 1)


emp_list = list(map(int, input("Enter employee IDs: ").split()))
emp_id = int(input("Enter employee ID to search: "))

found = find_employee(emp_list, emp_id, 0)

if found:
    print("Employee ID found")
else:
    print("Employee ID not found")
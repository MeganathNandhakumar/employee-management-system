import json

employees = []
next_id = 1


def save_employees():
    with open("employees.json", "w") as file:
        json.dump(employees, file, indent=4)


def load_employees():
    global employees, next_id

    try:
        with open("employees.json", "r") as file:
            employees = json.load(file)

        # Set the next ID based on existing employees
        if employees:
            next_id = max(employee["id"] for employee in employees) + 1
        else:
            next_id = 1

    except FileNotFoundError:
        employees = []
        next_id = 1

    except json.JSONDecodeError:
        print("Error: employees.json contains invalid data.")
        employees = []
        next_id = 1


def add_employee():
    global next_id

    print("\n--- Add Employee ---")

    name = input("Enter employee name: ").strip()

    if not name:
        print("Employee name cannot be empty.")
        return

    age = get_age()

    department = input("Enter employee department: ").strip()

    if not department:
        print("Department cannot be empty.")
        return

    salary = get_salary()

    employee = {
        "id": next_id,
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    }

    employees.append(employee)
    next_id += 1

    save_employees()

    print("Employee added successfully!")


def get_age():
    while True:
        age = input("Enter employee age: ")

        try:
            age = int(age)

            if age <= 0:
                print("Age must be greater than 0.")
            else:
                return age

        except ValueError:
            print("Please enter a valid number.")


def get_salary():
    while True:
        salary = input("Enter employee salary: ")

        try:
            salary = float(salary)

            if salary < 0:
                print("Salary cannot be negative.")
            else:
                return salary

        except ValueError:
            print("Please enter a valid salary.")


def display_employees():
    print("\n--- Employee List ---")

    if not employees:
        print("No employees found.")
        return

    for employee in employees:
        print("--------------------")
        print("ID:", employee["id"])
        print("Name:", employee["name"])
        print("Age:", employee["age"])
        print("Department:", employee["department"])
        print("Salary:", employee["salary"])


def search_employee():
    print("\n--- Search Employee ---")

    search_name = input("Enter employee name to search: ").strip()

    if not search_name:
        print("Search name cannot be empty.")
        return

    found = False

    for employee in employees:
        if employee["name"].lower() == search_name.lower():
            print("\nEmployee Found!")
            print("--------------------")
            print("ID:", employee["id"])
            print("Name:", employee["name"])
            print("Age:", employee["age"])
            print("Department:", employee["department"])
            print("Salary:", employee["salary"])

            found = True

    if not found:
        print("Employee not found.")


def update_employee():
    print("\n--- Update Employee ---")

    if not employees:
        print("No employees found.")
        return

    try:
        employee_id = int(input("Enter employee ID to update: "))

    except ValueError:
        print("Please enter a valid employee ID.")
        return

    for employee in employees:

        if employee["id"] == employee_id:

            print("\nCurrent employee information:")
            print("Name:", employee["name"])
            print("Age:", employee["age"])
            print("Department:", employee["department"])
            print("Salary:", employee["salary"])

            print("\nEnter new information.")
            print("Leave a field empty if you do not want to change it.")

            name = input("Enter new name: ").strip()

            if name:
                employee["name"] = name

            age = input("Enter new age: ").strip()

            if age:
                try:
                    age = int(age)

                    if age > 0:
                        employee["age"] = age
                    else:
                        print("Invalid age. Previous age kept.")

                except ValueError:
                    print("Invalid age. Previous age kept.")

            department = input("Enter new department: ").strip()

            if department:
                employee["department"] = department

            salary = input("Enter new salary: ").strip()

            if salary:
                try:
                    salary = float(salary)

                    if salary >= 0:
                        employee["salary"] = salary
                    else:
                        print("Invalid salary. Previous salary kept.")

                except ValueError:
                    print("Invalid salary. Previous salary kept.")

            save_employees()

            print("Employee updated successfully!")
            return

    print("Employee not found.")


def delete_employee():
    print("\n--- Delete Employee ---")

    if not employees:
        print("No employees found.")
        return

    try:
        employee_id = int(input("Enter employee ID to delete: "))

    except ValueError:
        print("Please enter a valid employee ID.")
        return

    for employee in employees:

        if employee["id"] == employee_id:

            print("\nEmployee found:")
            print("Name:", employee["name"])
            print("Department:", employee["department"])

            confirmation = input(
                "Are you sure you want to delete this employee? (yes/no): "
            ).strip().lower()

            if confirmation == "yes":
                employees.remove(employee)

                save_employees()

                print("Employee deleted successfully!")

            else:
                print("Delete operation cancelled.")

            return

    print("Employee not found.")


def main():
    while True:

        print("\n==============================")
        print("   Employee Management System")
        print("==============================")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_employee()

        elif choice == "2":
            display_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_employee()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            print("Thank you for using the Employee Management System.")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 6.")


# Load saved employees when the program starts
load_employees()

# Start the application
main()

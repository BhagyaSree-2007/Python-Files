'''Write a python program that reads data from a CSV file containing information
about employee (employee id, Name, Basic pay). Implement a function to calculate
total salary of an employee and display it to the user.'''
import csv

def calculate_total_salary(basic_pay):
    hra = 0.10 * basic_pay
    da = 0.05 * basic_pay
    return basic_pay + hra + da

def process_employee_data(file_path):
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            print(f"{'ID':<5} {'Name':<15} {'Basic':<10} {'Total Salary':<10}")
            print("-" * 45)

            for row in csv_reader:
                emp_id = row[0]
                name = row[1]
                basic_pay = float(row[2])
                total_salary = calculate_total_salary(basic_pay)
                print(f"{emp_id:<5} {name:<15} {basic_pay:<10.2f} {total_salary:<10.2f}")

    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
process_employee_data('employees.csv')

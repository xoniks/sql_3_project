from employee_management import add_employee
from wage_calculation import calculate_and_record_wage, calculate_wages_from_file


def main():
    while True:
        print("1. Add Employee")
        print("2. Calculate Wage Manually")
        print("3. Calculate wage from a file")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice=='1':
            name = input('Enter employees name: ')
            rate = float(input("Enter hourly rate: "))
            add_employee(name,rate)
            print('Employee added')
        
        elif choice=='2':
            employee_id = int(input('Enter employees id: '))
            date = input("Enter date (YYYY-MM-DD): ")
            hours_worked = float(input("Enter hours worked: "))
            calculate_and_record_wage(employee_id,date,hours_worked)
            print('Wage calculcated')
            
        elif choice == '3':
            # print('This feature is not available right now :)')
            # continue
            file_path = input('Please enter the file path: ')
            calculate_wages_from_file(file_path)
        
        elif choice == '4':
            print('Exiting...')
            break
        
        else:
            print('Invalid choice. Please try again!')
            
print('Before main')

if __name__=='__main__':
    main()
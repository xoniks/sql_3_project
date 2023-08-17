import sqlite3

def calculate_and_record_wage(employee_id, date, hours_worked):
    conn = sqlite3.connect('wage_payment.db')
    c = conn.cursor()
    
    c.execute(' Select rate From employees Where id = ?',(employee_id,))
    rate = c.fetchone()[0]
    
    amount_paid = rate * hours_worked
    
    c.execute('Insert Into wages (employee_id, date, hours_worked, amount_paid) Values (?,?,?,?)',
              (employee_id, date, hours_worked, amount_paid))
    
    conn.commit()
    conn.close()
    
def calculate_wages_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:
            print(line)
            employee_id, date, hours_worked = line.strip().split(',')
            calculate_and_record_wage(int(employee_id), date, float(hours_worked))
        